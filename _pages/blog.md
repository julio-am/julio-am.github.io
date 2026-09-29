---
layout: page
title: blog
permalink: /blog/
description: Research notes, ideas, and things I am learning.
nav: true
nav_order: 3
pagination:
  enabled: true
  collection: posts
  permalink: /page/:num/
  per_page: 5
  sort_field: date
  sort_reverse: true
  trail:
    before: 1
    after: 3
---

<ul class="personal-post-list">
{% for post in paginator.posts %}
  <li>
    <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
    <p>{{ post.description }}</p>
    <div class="post-meta">
      <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: '%B %-d, %Y' }}</time>
      <span aria-hidden="true"> · </span>
      {{ post.content | number_of_words | divided_by: 180 | plus: 1 }} min read
    </div>
  </li>
{% endfor %}
</ul>

{% include pagination.liquid %}

<p class="feed-link"><a href="{{ '/feed.xml' | relative_url }}">Subscribe via RSS</a></p>
