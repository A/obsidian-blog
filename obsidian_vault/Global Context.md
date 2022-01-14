### Global Context

`global_context` is always accessible in all handlebars templates (layouts, pages)  and includes few variables:

```
{
  "config": {
    "ASSETS_PATH": "/${ASSETS_DEST_DIR}",
    "BLOG_TITLE": BLOG_TITLE,
  },
  "layouts": dict[str, Layout],
  "posts": list[Post],
  "pages": list[Page],
})
```

For pages and posts global context is merged with `page_context` and `post_context` accordingly.