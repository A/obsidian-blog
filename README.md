## Obsidian SSG Blog

Experiments around static site generation for obsidian markdown

The idea is to create a simple blog generated from obsidian [Map Of Content][moc]
notes, that's I believe based on the [original zettelkasten benefit][zettelkasten].

### Env

`obsidian-blog` expects you have an `.env` file, contains given variables:

  - `SOURCE_DIR` — is a directory contains a blog posts, pages, layouts, and assets.
  - `DEST_DIR` — is a directory `obsidian-blog` builds static site to.
  - `BLOG_TITLE` — is a default `<title>` attr.

### Blog files

```
 @A/notes ❯ tree _blog
_blog
├── Article 1.md
├── Article 2.md
├── _assets
│   └── styles.css
├── _layouts
│   └── main.hbs
└── _pages
    ├── about.hbs
    └── index.hbs
```

### Posts

Posts are just md-files in the root blog directory, each post should have meta-data like below:

```
---
title: My awesome post (<title> attr)
date: 2021-01-01 (used for sorting)
layout: main (a layout name from `_layouts` used to render a post)
---
```

### Pages

Pages are handlebars templates, rendered with a context contains `title` and `posts[]` properties.

### Assets

All the files from `${SOURCE_DIR}/_assets` directory are copied automatically to the `${DEST_DIR}/assets` during the build,
so this files are accessible via `/assets/<file>` urls


[moc]: https://www.youtube.com/watch?v=7GqQKCT0PZ4
[zettelkasten]: https://en.wikipedia.org/wiki/Niklas_Luhmann#Note-taking_system_(Zettelkasten)
