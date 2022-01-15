## Environment variables

`.env`-file is a way to configure your blog. This is the list of supported env-vars:

- `BLOG_TITLE` (default: `None`)
- `DEST_DIR` (default: `_build`) is a directory your blog is build to.
- `SOURCE_DIR` (default: `_blog`) is a root directory of your blog.
- `LAYOUTS_DIR` (default: `${SOURCE_DIR}/_layouts`) for handlebars layouts.
- `PAGES_DIR` (default: `${SOURCE_DIR}/_pages`) for handlebars pages.
- `ASSETS_DIR` (default: `${SOURCE_DIR}/_assets`) for static files to be copied into the build.
- `ASSETS_DEST_DIR` (default: `static`) this is the path under `DEST_DIR` your static files and images from the posts are copied to.
