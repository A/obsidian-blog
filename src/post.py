import frontmatter
from src.helpers import get_slug
from src.image import Image
from src.include import Include


class Post():
  @staticmethod
  def load(filename):
    f = frontmatter.load(filename)
    if f.metadata.get("published"):
      return Post(
        filename=filename,
        meta=f.metadata,
        content=f.content,
        images=Image.get_all(f.content),
        includes=Include.get_all(f.content),
      )
    return Post.get_private_post(filename=filename, meta=f.metadata)
  
  @staticmethod
  def get_private_post(filename, meta):
    return Post(
      filename=filename,
      meta=meta,
      content="",
      images=[],
      includes=[],
    )

  def __init__(self, filename, meta, content, images, includes):
    self.filename = filename
    self.meta = meta
    self.content = content
    self.images = images
    self.includes = includes
    self.slug = get_slug(self)

  def render(self):
    content = self.content
    content = Image.render_all(self, content)
    content = Include.render_all(self, content)
    return content
