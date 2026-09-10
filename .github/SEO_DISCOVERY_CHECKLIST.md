# Search and AI discovery checklist

The repository now supplies crawlable, human-readable evidence plus structured data. No markup can guarantee inclusion or rank in an LLM answer; authority, query fit, external corroboration, crawl timing, and each provider's retrieval system still matter.

## After reviewing and deploying

- Confirm that `https://sadmanahmedshanto.com/`, `/sitemap.xml`, `/robots.txt`, `/llms.txt`, `/llms-full.txt`, `/assets/json/profile.json`, and `/research/ai-for-science/` return HTTP 200.
- Confirm that the homepage, publications page, SQuADDS project, and AI-for-science page use `sadmanahmedshanto.com` canonicals and contain valid JSON-LD.
- Add the domain property to Google Search Console, verify it through DNS, and submit `https://sadmanahmedshanto.com/sitemap.xml`.
- Add or import the site in Bing Webmaster Tools and submit the same sitemap. Bing coverage also benefits Microsoft Copilot discovery.
- Use Google URL Inspection and Bing URL Inspection for the homepage, SQuADDS project, publications, and AI-for-science page after the first deployment.
- Keep Google and Bing verification tokens in `_config.yml`, then enable the corresponding flags. Do not commit DNS credentials or account secrets.

## External corroboration

Use the same canonical name, current status, and website URL on:

- USC Physics and Levenson-Falk Lab profiles
- ORCID and Google Scholar
- GitHub profile and the SQuADDS organization/repository
- LinkedIn and ResearchGate
- Hugging Face SQuADDS dataset card
- SQuADDS documentation and package metadata
- conference, workshop, and invited-talk pages when organizers permit edits

Prefer links from those records back to the canonical website, SQuADDS paper, code, dataset, and ORCID. Describe Google Quantum AI and Quantum Elements as former internships with dates. Do not repeat private or unverifiable claims merely to increase keyword frequency.

## Indexing and change notifications

- Search engines can discover changes through the sitemap. For Bing and other IndexNow participants, create an IndexNow key, host the required key text file at the domain root, and submit changed public URLs through the official IndexNow endpoint.
- Search Console submission, Bing verification, and IndexNow require account ownership or a key and therefore are intentionally not automated by this repository.
- Update the dates and facts in `profile.json`, `resume.json`, `llms.txt`, and `llms-full.txt` together whenever status changes.

## Monthly benchmark

- Run the queries in `.github/ai-discovery-queries.yml` against each listed provider.
- Save exact outputs and citations outside the public site, compare three runs per query, and track discovery rate, entity accuracy, source quality, and stale claims.
- Treat movement as noisy unless it persists across providers and repeated runs.
- When a gap appears, add or improve genuine public evidence at the most relevant existing page. Do not use hidden text, cloaking, doorway pages, fabricated awards, or unsupported ranking claims.
