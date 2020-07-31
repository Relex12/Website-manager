---
layout: default
title: "Projects"
---

# {{ page.title }}

Insérer la liste des projets.

Test 1 :

{% for link in site.navigation %}
  * [{{ link.title }}]({{ link.url }})
{% endfor %}

Test 2 :
<!-- Peut sûrement être opimisé -->
{% for link in site.navigation %}
  {% if link.title == page.title and link.sons %}
    {% for link2 in link.sons %}
  * [{{ link2.title }}]({{ link2.url }})      
    {% endfor %}
  {% endif %}
{% endfor %}
