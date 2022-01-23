import glob
import os
import re

from slugify.slugify import slugify

from obsidian_blog import markdown
from lib.logger import log
from obsidian_blog.helpers import normalize_path

IMG_REF_PREFIX = "__image__"
MW_IMG_REGEXP = r'(\!\[\[(.*)\]\])'
MD_INLINE_IMG_REGEXP = r'(\!\[(.*)\]\((.*)\))'
MD_REFERENCE_IMAGE = r'(\!\[(.*)]\[(.*)\])'
IMAGE_EXTENSIONS = ['.png']

class Image:

  def __init__(self, placeholder, alt, filename):
    self.placeholder = placeholder
    self.alt = alt
    self.filename = filename
    
  @staticmethod
  def create(placeholder, alt, filename):
    return Image(placeholder=placeholder, alt=alt, filename=filename)
  
  @staticmethod
  def get_all(content):
    md_imgs = Image.get_md_inline_images(content)
    reference_md_imgs = Image.get_md_reference_images(content)
    mw_imgs = Image.get_mw_images(content)
    return [
      *md_imgs,
      *reference_md_imgs,
      *mw_imgs,
    ]

  @staticmethod
  def get_md_inline_images(content):
    matches = re.findall(MD_INLINE_IMG_REGEXP, content)
    inline_images = map(lambda match: Image.create(*match), matches)
    return [*inline_images]

  @staticmethod
  def get_md_reference_images(content):
    reference_images = []
    matches = re.findall(MD_REFERENCE_IMAGE, content)

    for match in matches:
      placeholder, alt, id = match
      link_re = re.compile("\\[" + id + "\\]:\\s(.*)")
      filenames = re.findall(link_re, content)
      reference_images.append((placeholder, alt, normalize_path(filenames[0]) or ''))

    return map(lambda img: Image.create(*img), reference_images)

  @staticmethod
  def get_mw_images(content):
    mw_images = []
    matches = re.findall(MW_IMG_REGEXP, content)

    for match in matches:
      placeholder = match[0]
      alt = match[1]

      try:
        filename, *_ = glob.glob(f"**/{alt}", recursive=True)
        mw_images.append((placeholder, alt, filename))
      except:
        print(f"Image \"{alt}\" not found ")

    return map(lambda img: Image.create(*img), mw_images)

  @staticmethod
  def get_mw_image(content):
    matches = glob.glob('**/' + name + '.md', recursive=True)

  @staticmethod
  def render_all(parent, parent_content):
    for image in parent.images: parent_content = image.render(parent, parent_content)
    return Image.cleanup_refs(parent_content)

  @staticmethod
  def cleanup_refs(content):
    refs_re = r"\[(.*)\]:\s.*"
    refs = re.findall(refs_re, content)
    for id in refs:
      content = Image.cleanup_duplicated_ref_ids(id, content)
      content = Image.cleanup_unused_ref_id(id, content)
    return content

  @staticmethod
  def cleanup_duplicated_ref_ids(id, content: str):
    link_re = re.compile("(\\[" + id + "\\]:\\s.*[\r\n]{0,})")
    matches = re.findall(link_re, content)
    if len(matches) > 1:
      del matches[0]

      for placeholder in matches:
        content = content.replace(placeholder, "", 1)
    return content

  @staticmethod
  def cleanup_unused_ref_id(id, content):
    link_re = re.compile("\\!\\[.*\\]\\[" + id + "\\]")
    matches = re.findall(link_re, content)
    if not len(matches):
      ref_re = re.compile("(\\[" + id + "\\]:\\s.*)")
      placeholders = re.findall(ref_re, content)
      for placeholder in placeholders:
        content = content.replace(placeholder, "")
    return content

  @staticmethod
  def is_image(filename):
    _, ext = os.path.splitext(filename)
    if ext in IMAGE_EXTENSIONS:
      return True
    return False

  def render(self, parent, parent_content):
    prefix = slugify(parent.meta.get("title"))
    content = parent_content.replace(
      self.placeholder,
      f"![{self.alt}][{prefix}.{self.alt}]",
    )
    content = f"{content}\n[{prefix}.{self.alt}]: {self.filename}"
    return content
