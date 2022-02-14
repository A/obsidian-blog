## Obsidian SSG Blog

**DISCLAIMER: Still work-in-progress, so API definitely will change. To use it you'd better to have some programming experience**

The idea is to create a simple blog generated from obsidian [Map Of Content][moc]
notes [original zettelkasten benefit][zettelkasten].

### Features

- Yet another static site generator for obsidian.
- Built to use with git, github pages and action.
- Uses handlebars template engine
- Supports `--watch` and `--serve` modes for local writing
- Recursively parses [[includes]] and has cycles detection
- Automatically copies included local images into the build
- Supports `--drafts` mode to work unpublished files locally
- Privacy. Notes can be published only with explicit `published: True` annotation.
- Fluent title detection from [[note | alt title]], frontmatter `title` attribute, or a filename.
- Render notes as links, in case they're included in the middle of the paragraph and have `link` frontmatter attribute.
- Supports filename delimeters: `Topic - Category - Note` becomes just `Note`

### Installation

```
pip install obsidian-blog
```

### Usage

```
$ obsidian-blog -h
obsidian-blog

Static site generator for obsidian.md notes.

Usage:
  obsidian-blog [-d] [-w] [-s] [--port <number>] [--title <string>] [--posts_dir <directory>] [--pages_dir <directory>]

Options:
  -h --help                     Show this screen.
  -w --watch                    Enable watcher
  -s --serve                    Enable web-server
  -p --port=<number>            Web-server port [default: 4200]
  -d --drafts                   Render draft pages and posts

  --title=<string>              Blog title [default: My Blog]

  --version             Show version.
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
│       └── main.hbs # name of layout, can be selected with `layout` frontmatter attribute. Default: `main`
├── .build # build directory created by run `obsidian-blog` to be deployed
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

### Feedback and things

Just text me in [telegram][tg] or file an issue. I'd be happy to know if you want to use it.

### Alternatives

- [Obsidian Export][obsidian-export] - cli to render obsidian notes into markdown written in Rust

[moc]: https://www.youtube.com/watch?v=7GqQKCT0PZ4
[zettelkasten]: https://en.wikipedia.org/wiki/Niklas_Luhmann#Note-taking_system_(Zettelkasten)
[my-blog]: https://anto.sh
[obsidian-blog-theme]: https://github.com/A/obsidian-blog-theme/
[tg]: https://t.me/a_shuvalov
[obsidian-export]: https://crates.io/crates/obsidian-export
