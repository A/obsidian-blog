import os
import re
import glob
import frontmatter
from slugify import slugify

from lib import fs, config, handlebars, markdown
from lib.logger import log
from lib.models.Image import Image
from lib.models.Include import Include, IncludeMeta
from lib.models.Layout import Layout
from lib.models.Meta import Meta
from lib.models.Post import Post
from lib.models.Page import Page


def unwrap_markdown(md_str: str):
  """unwrap images and includes in the given markdown string"""
  res = md_str
  res = unwrap_includes(res)
  return res


def replace_image_urls(md: str, imgs: list[Image], url_prefix: str = "/"):
  res = md
  for img in imgs:
    placeholder = img.get("placeholder")
    name = img.get("name")
    slug = img.get("slug")
    img_str = "![" + name + "]("+ url_prefix + "/" + slug +"){: width='100%'}"
    res = res.replace(placeholder, img_str)
  return res


def get_post(file: str):
  post = frontmatter.load(file)
  log("Prepare a post:", post.metadata.get("title"))
  includes = get_all_includes(post.content)
  md = unwrap_markdown(post.content)
  imgs = get_all_images(md)
  md = replace_image_urls(md, imgs, "/" + config.ASSETS_DEST_DIR)

  slug = (post.metadata.get("slug") or slugify(fs.change_ext("", fs.basename(file)))) + ".html"
  html = markdown.parse_markdown(md)

  return Post(
    file = file,
    html = html,
    meta = Meta(**post.metadata),
    slug = slug,
    imgs = imgs,
    includes = includes,
  )


def get_posts():
  """Returns all posts in the given directory"""
  posts = []
  files = fs.get_files_in_dir(config.SOURCE_DIR, filter_partials=True)

  for file in files:
    post = get_post(os.path.join(config.SOURCE_DIR, file))
    posts.append(post)

  return sorted(posts, key=lambda p: p.get("meta").get("date"),  reverse=True)

def get_page(file: str):
  page = frontmatter.load(file)
  slug = slugify(fs.change_ext("", fs.basename(file))) + ".html"

  _, ext = os.path.splitext(file)
  if ext == ".md":
    print("MARKDOWN")
    page.content = markdown.parse_markdown(page.content)


  page = Page(
    meta = Meta(**page.metadata),
    slug = slug,
    template = handlebars.create_template_fn(page.content),
    file = file,
  )

  return page


def get_pages():
    """returns all hbs pages in the given dir"""
    pages: list[Page] = []

    files = fs.get_files_in_dir(config.PAGES_DIR, filter_partials=True)

    for file in files:
      page = get_page(os.path.join(config.PAGES_DIR, file))
      pages.append(page)
    
    return pages


def get_all_includes(content: str) -> list[Include]:
    """Returns a list of all obsidian includes"""

    matches = re.findall(config.MEDIAWIKI_INCLUDE_REGEXP, content)
    return list(filter(
        lambda include: include is not None,
        map(get_include, matches)
    ))


def get_include(name: str) -> Include:
    """Returns a parsed include meta and content"""
    matches = glob.glob('**/' + name + '.md', recursive=True)
    file = matches[0] if len(matches) > 0 else None
    placeholder = "[[" + name + "]]"

    if file == None: return None

    include = frontmatter.load(file)
    meta = IncludeMeta(**include.metadata)

    if not meta.get("published"): return None

    return Include(
      file = file,
      name = name,
      meta = meta,
      content = include.content,
      placeholder = placeholder
    )


def get_all_images(content: str) -> list[Image]:
  matches = re.findall(config.MEDIAWIKI_IMG_REGEXP, content)
  return list(filter(
    lambda img: img is not None,
    map(get_image, matches)
  ))


def get_image(file: str):
  """Returns a parsed include meta and content"""

  matches = glob.glob('**/' + file, recursive=True)
  if len(matches) == 0: return None
  match = matches[0]

  name, ext = os.path.splitext(fs.basename(match))
  slug = slugify(name) + ext


  return Image(
    slug = slug,
    name = name,
    file = match,
    placeholder = "![[" + file + "]]",
  )

def unwrap_includes(content: str):
    result = content
    for include in get_all_includes(result):
      log("  Unwrapping an include:", include.get("name"))
      html = render_include(include)
      result = result.replace(include.get("placeholder"), html)
    return result

def render_include(include: Include):
  title = include.get("meta").get("title") or None
  content = include.get("content")
  header = ""
  if title:
    header = "<h3 class='subheader' id='" + title + "'><a href='#" + title +"'>" + title  +"</a></h3>\n"
  return header + content + "\n"

def get_layout(file: str) -> Layout:
  name, _ = os.path.splitext(fs.basename(file))
  with open(file) as f: hbs_str = f.read()
  return Layout(
    name = name,
    template = handlebars.create_template_fn(hbs_str)
  )

def get_layouts() -> dict[str, Layout]:
    """return dict by name of all hbs layouts from a given dir"""
    layouts: dict[str, Layout] = {}

    files = fs.get_files_in_dir(config.LAYOUTS_DIR, filter_partials=True)
    for file in files:
      layout = get_layout(os.path.join(config.LAYOUTS_DIR, file))
      layouts[layout.get("name")] = layout

    return layouts
