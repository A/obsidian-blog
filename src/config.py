# pyright: strict
from os import path
from dotenv.main import dotenv_values

_env = dotenv_values('.env')

BLOG_TITLE = _env.get("BLOG_TITLE") or "My Blog"
DEST_DIR = _env.get("DEST_DIR") or ".build"
SOURCE_DIR = _env.get("SOURCE_DIR") or ".blog"
POSTS_DIR = _env.get("POSTS_DIR") or "Posts"
PAGES_DIR = _env.get("PAGES_DIR") or path.join("Pages")
LAYOUTS_DIR = _env.get("LAYOUTS_DIR") or path.join(SOURCE_DIR, "_layouts")
ASSETS_DIR = _env.get("ASSETS_DIR") or path.join(SOURCE_DIR, "_assets")
ASSETS_DEST_DIR = _env.get("ASSETS_DEST_DIR") or "static"
VERBOSE = _env.get("VERBOSE") or False
DEFAULT_LAYOUT = "main"
