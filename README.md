## Obsidian SSG Blog

**DISCLAIMER: Still work-in-progress, so API definitely will change. To use it you'd better to have some programming experience**

Experiments around static site generation for obsidian markdown. 

The idea is to create a simple blog generated from obsidian [Map Of Content][moc]
notes, that's I believe based on the [original zettelkasten benefit][zettelkasten].

### Usage

```
cd <your-obsidian-vault>
obsidian-blog
```

### Example

See [Obsidian Blog Theme][obsidian-blog-theme]

### Env

`obsidian-blog` expects you have an `.env` file. Supported variables and their default values can be found
in `src/dataclasses/config_data`.

### Blog files

```
notes ❯ tree .blog -a -I .git
├── .blog
│   ├── _assets # static files to be copied into .build
│   │   └── styles.css
│   └── _layouts # layout files
│       └── main.hbs
├── .build # build directory created by run `obsidian-blog` and to be deployed
├── .env # environment variables
├── Pages # Pages directory, contains handlebars and markdown files
└── Posts # Posts directory contains obsidian markdown files (which are anyway processed via handlebars)
```


### Posts

Posts are obsidian markdown files with includes, images, and anything you usually have in your obsidian notes.
Posts are post-processed by handlebars, so you can use it if you need (but not sure if it's a good idea tho).

```
---
title: My awesome post
date: 2021-01-01 (used for sorting)
published: True # privacy, can't be skipped
layout: main (default_layout is used if it skipped)
---
```

### Pages

Pages are handlebars templates (or just markdown files), rendered via global (`pages` and `posts` lists) and local (`self` points
to the entity being rendered) contexts.

### Assets

Assets are divided into 2 types:
- `.blog/_assets` copyed during the build unconditionally
- Images insluded either with markdown reference or incline images, or by obsidian ![[<file>]] syntax. This ones are detected and copyed during the build.

### Deployment

So far I'm using github actions to deploy my stuff to [my blog][my-blog].

[moc]: https://www.youtube.com/watch?v=7GqQKCT0PZ4
[zettelkasten]: https://en.wikipedia.org/wiki/Niklas_Luhmann#Note-taking_system_(Zettelkasten)
[my blog]: https://anto.sh
[obsidian-blog-theme]: https://github.com/A/obsidian-blog-theme/
