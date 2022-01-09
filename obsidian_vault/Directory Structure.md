### Directory Structure

The first thing you need to do is to create a `_blog` directory in the root of your vault with a structure like on the listing below. The simplest way is to copy it from this example vault. 

```
_blog
├── Post.md
├── _assets
│   └── styles.css
├── _layouts
│   └── main.hbs
└── _pages
    ├── about.hbs
    └── index.hbs
```

Now let me briefly explain each directory inside of `_blog`:
- `_assets` are static files, such as `css`, `js` or images are always being copied into resulting build.
- `_layouts` is a room for handlebars layout files. You can specify different layouts for diferent pages and posts by setting `layout: <layout_name>` in the [yaml-frontmatter][frontmatter] part of the file.
- `_pages` is where handlebars page templates live. Like `about`, `contacts`, `all-posts`, `my cv` and so on.

Note, that there is no `posts` directory, because, all your posts lives right inside the `_blog` directory.