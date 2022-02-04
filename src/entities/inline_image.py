import re
from src.entities.page_data import PageData

INLINE_IMG_RE = r'(\!\[(.*)\]\((.*)\))'

class InlineImage:

  def __init__(self, placeholder, alt, filename):
    self.placeholder = placeholder
    self.alt = alt
    self.filename = filename

  @staticmethod
  def get_all(data: PageData):
    # TODO: Skip by entity instance?
    if not hasattr(data, "content"): return []

    parent_content = data.content
    matches = re.findall(INLINE_IMG_RE, parent_content)
    return list(map(lambda match: InlineImage(*match), matches))

  @staticmethod
  def render_one(data: PageData, entity: "InlineImage"):
    if not isinstance(entity, InlineImage): return
    rendered_image = f"[{entity.alt}]({entity.filename})"
    return data.content.replace(entity.placeholder, rendered_image)
