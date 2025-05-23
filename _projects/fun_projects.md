---
layout: page
title: Personal Projects
description: not as serious as it sounds
img: assets/img/logo.png
importance: 7
category: fun
giscus_comments: true
---

One thing I need to work on is to have more complex projects that take a good amount of time to build because all I have here are projects that I have built in a few hours or days....

<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% for repo in site.data.repositories.github_repos %}
    {% include repository/repo.liquid repository=repo %}
  {% endfor %}
</div>