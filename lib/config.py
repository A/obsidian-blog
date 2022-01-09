# pyright: strict
from os import path
from dotenv.main import dotenv_values

_env = dotenv_values('.env')

BLOG_TITLE = _env.get("BLOG_TITLE") or "My Blog"
DEST_DIR = _env.get("DEST_DIR") or "_build"
SOURCE_DIR = _env.get("SOURCE_DIR") or "_blog"
LAYOUTS_DIR = _env.get("LAYOUTS_DIR") or path.join(SOURCE_DIR, "_layouts")
PAGES_DIR = _env.get("PAGES_DIR") or path.join(SOURCE_DIR, "_pages")
ASSETS_DIR = _env.get("ASSETS_DIR") or path.join(SOURCE_DIR, "_assets")
