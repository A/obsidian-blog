### Layouts

Layouts are old good handlebars layouts compiled with a `global_context` and `page_context` or `post_context` accordingly. There is a simple example layout renders links to all pages and a content.

```html
<!DOCTYPE html>

<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>{{ title }}</title>
    <link rel="stylesheet" href="{{ config.ASSETS_PATH }}/styles.css">
  </head>
  <body>
    <h1 class="menu__header">
      <a href=/>{{ config.BLOG_TITLE }}</a>
    </h1>
    <div class="menu">
      <ul class="links">
        {{#each pages}}
          <li class="link">
            <a href="/{{this.slug}}">{{this.meta.title}}</a>
          </li>
        {{/each}}
      </ul>
    </div>
    <div class="content">
      <div class="page">
        {{{ content }}}
      </div>
    </div>
  </body>
</html>
```

In a post or a page, you can specify which one you'd like to use to render the content within the yaml-frontmatter block:

```
---
title: Hello World
date: 2021-01-09
layout: main
---
```

If layout is not specified, `main` will be used as default one.