---
layout: page
title: Quantum Wells and Resonant Tunneling
description: Solid State Course @ USC
img: assets/img/research/academic/ss_thumbnail.png
importance: 5
category: classes
giscus_comments: true
toc:
  sidebar: left
---

**Fall 2022**

{% assign jupyter_path = 'assets/jupyter/solid_state_presentation.ipynb' | relative_url %}
{% capture notebook_exists %}{% file_exists assets/jupyter/solid_state_presentation.ipynb %}{% endcapture %}
{% if notebook_exists == 'true' %}
  {% jupyter_notebook jupyter_path %}
{% else %}
  <p>Sorry, the notebook you are looking for does not exist.</p>
{% endif %}