---
layout: page
title: projects
permalink: /projects/
description: A place for ongoing work, experiments, and collaborations.
nav: true
nav_order: 2
---

<ul class="project-list">
{% assign sorted_projects = site.projects | sort: 'importance' %}
{% for project in sorted_projects %}
  <li>
    <h2><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h2>
    <p>{{ project.description }}</p>
    <span class="project-category">{{ project.category }}</span>
  </li>
{% endfor %}
</ul>
