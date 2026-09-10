#!/usr/bin/env python3
"""End-to-end regression tests for publication synchronization."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[1]
SYNC = REPOSITORY / "bin" / "sync-arxiv-publications"


DISCOVERY_FEED = b"""<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom">
  <entry>
    <id>https://arxiv.org/abs/2609.12345v1</id>
    <published>2026-09-09T00:00:00Z</published>
    <title>New Automated Discovery</title>
    <summary>A new research result discovered by the synchronizer.</summary>
    <author><name>A. Researcher</name></author>
    <author><name>S. A. Shanto</name></author>
    <arxiv:primary_category term="quant-ph" />
  </entry>
  <entry>
    <id>https://arxiv.org/abs/2401.00001v2</id>
    <published>2024-01-01T00:00:00Z</published>
    <title>Existing Paper</title>
    <summary>An existing paper whose arXiv identifiers were absent.</summary>
    <author><name>Sadman Ahmed Shanto</name></author>
    <arxiv:primary_category term="quant-ph" />
  </entry>
</feed>
"""


ACCEPTANCE_FEED = b"""<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom">
  <entry>
    <id>https://arxiv.org/abs/2501.00002v3</id>
    <published>2025-01-02T00:00:00Z</published>
    <title>Paper That Became a Journal Article</title>
    <summary>A paper that was initially listed as under review.</summary>
    <author><name>Researcher One</name></author>
    <author><name>Sadman Shanto</name></author>
    <arxiv:primary_category term="quant-ph" />
    <arxiv:doi>10.1234/example.2026.42</arxiv:doi>
    <arxiv:journal_ref>Journal of Reliable Tests 12, 42 (2026)</arxiv:journal_ref>
  </entry>
</feed>
"""


CROSSREF_RECORD = {
    "10.1234/example.2026.42": {
        "DOI": "10.1234/example.2026.42",
        "type": "journal-article",
        "title": ["Paper That Became a Journal Article"],
        "author": [
            {"given": "Researcher", "family": "One"},
            {"given": "Sadman", "family": "Shanto"},
        ],
        "container-title": ["Journal of Reliable Tests"],
        "publisher": "Test Society",
        "volume": "12",
        "issue": "3",
        "page": "42-50",
        "published-online": {"date-parts": [[2026, 8, 15]]},
    }
}


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def create_site(root: Path, title: str = "Existing Paper", arxiv_id: str = "") -> None:
    (root / "_bibliography").mkdir(parents=True)
    (root / "_data").mkdir(parents=True)
    (root / "assets/json").mkdir(parents=True)
    arxiv_fields = ""
    if arxiv_id:
        arxiv_fields = (
            f"  eprint = {{{arxiv_id}}},\n"
            "  archivePrefix = {arXiv},\n"
            "  primaryClass = {quant-ph},\n"
        )
    (root / "_bibliography/papers.bib").write_text(
        "@string{aps = {American Physical Society}}\n\n"
        "@Article{existing,\n"
        f"  title = {{{title}}},\n"
        "  author = {Sadman Ahmed Shanto},\n"
        "  year = {2025},\n"
        f"{arxiv_fields}"
        "  selected = {true},\n"
        "}\n",
        encoding="utf-8",
    )
    write_json(
        root / "assets/json/resume.json",
        {
            "publications": [
                {
                    "name": title,
                    "publisher": "Under Review at Journal of Reliable Tests",
                    "releaseDate": "2025",
                    "summary": "Research result under review at Journal of Reliable Tests.",
                }
            ]
        },
    )
    write_json(
        root / "assets/json/profile.json",
        {
            "@type": "Person",
            "mainEntityOfPage": {"dateModified": "2025-01-01"},
            "subjectOf": [{"@type": "ScholarlyArticle", "name": title}],
        },
    )
    write_json(root / "_data/publications.json", [])
    (root / "llms-full.txt").write_text(
        "# Selected Publications\n\n"
        f"- **{title}** (*Shanto*) — Under Review, 2025\n\n"
        "# Next Section\n",
        encoding="utf-8",
    )
    (root / "llms.txt").write_text(
        "# Profile\n\n"
        "   - Publications: https://example.com/an-old-paper\n",
        encoding="utf-8",
    )


def run_sync(root: Path, feed: Path, *extra: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            "-B",
            str(SYNC),
            "--root",
            str(root),
            "--feed-file",
            str(feed),
            *extra,
        ],
        check=True,
        capture_output=True,
        text=True,
    )


class SyncArxivPublicationsTest(unittest.TestCase):
    def test_discovers_propagates_and_is_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            create_site(root)
            feed = root / "feed.xml"
            feed.write_bytes(DISCOVERY_FEED)

            first = run_sync(root, feed, "--skip-crossref")
            first_snapshot = {
                path.relative_to(root): path.read_bytes()
                for path in root.rglob("*")
                if path.is_file() and path != feed
            }

            self.assertIn("New Automated Discovery", first.stdout)
            bibliography = (root / "_bibliography/papers.bib").read_text(encoding="utf-8")
            self.assertEqual(bibliography.count("Existing Paper"), 1)
            self.assertIn("eprint = {2401.00001}", bibliography)
            self.assertIn("eprint = {2609.12345}", bibliography)

            resume = json.loads((root / "assets/json/resume.json").read_text(encoding="utf-8"))
            profile = json.loads((root / "assets/json/profile.json").read_text(encoding="utf-8"))
            machine_data = json.loads((root / "_data/publications.json").read_text(encoding="utf-8"))
            for identifier in ("2401.00001", "2609.12345"):
                self.assertTrue(any(item.get("arxiv") == identifier for item in resume["publications"]))
                self.assertTrue(
                    any(identifier in json.dumps(item) for item in profile["subjectOf"])
                )
                self.assertTrue(any(item.get("arxiv") == identifier for item in machine_data))
            self.assertIn(
                "https://sadmanahmedshanto.com/publications/",
                (root / "llms.txt").read_text(encoding="utf-8"),
            )
            self.assertIn(
                "arXiv:2609.12345",
                (root / "llms-full.txt").read_text(encoding="utf-8"),
            )

            second = run_sync(root, feed, "--skip-crossref")
            second_snapshot = {
                path.relative_to(root): path.read_bytes()
                for path in root.rglob("*")
                if path.is_file() and path != feed
            }
            self.assertIn("No publication changes", second.stdout)
            self.assertEqual(first_snapshot, second_snapshot)

    def test_replaces_preprint_status_with_crossref_journal_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            create_site(root, "Paper That Became a Journal Article", "2501.00002")
            feed = root / "feed.xml"
            crossref = root / "crossref.json"
            feed.write_bytes(ACCEPTANCE_FEED)
            write_json(crossref, CROSSREF_RECORD)

            result = run_sync(root, feed, "--crossref-file", str(crossref))
            self.assertIn("Journal of Reliable Tests", result.stdout)

            bibliography = (root / "_bibliography/papers.bib").read_text(encoding="utf-8")
            self.assertIn("doi = {10.1234/example.2026.42}", bibliography)
            self.assertIn("journal = {Journal of Reliable Tests}", bibliography)
            self.assertIn("volume = {12}", bibliography)
            self.assertIn("pages = {42-50}", bibliography)

            resume = json.loads((root / "assets/json/resume.json").read_text(encoding="utf-8"))
            publication = resume["publications"][0]
            self.assertEqual(publication["publisher"], "Journal of Reliable Tests")
            self.assertEqual(publication["doi"], "10.1234/example.2026.42")
            self.assertNotIn("under review", publication["summary"].lower())

            profile = json.loads((root / "assets/json/profile.json").read_text(encoding="utf-8"))
            article = next(
                item for item in profile["subjectOf"] if item.get("@type") == "ScholarlyArticle"
            )
            self.assertEqual(article["@id"], "https://doi.org/10.1234/example.2026.42")
            self.assertEqual(article["isPartOf"]["name"], "Journal of Reliable Tests")


if __name__ == "__main__":
    unittest.main()
