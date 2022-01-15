### Pages

Pages are handlebars templates support a yaml-frontmatter section. Pages stands for anything but posts. 

This is an example of `index.hbs` page renders all posts from the blog:

```handlebars
---
title: Posts
---
<h1>{{ meta.title }}</h1>
<ul>
  {{#each posts}}
      <li>
        <span>[{{ this.meta.date }}]: </span>
        <a href={{this.slug}}>{{ this.meta.title }}</a>
      </li>
  {{/each}}
</ul>

```
