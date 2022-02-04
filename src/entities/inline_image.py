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
    if not hasattr(data, "content"): return []

    parent_content = data.content
    matches = re.findall(INLINE_IMG_RE, parent_content)
    return list(map(lambda match: InlineImage(*match), matches))

  def render(self, data: PageData):
    content = data.content
    rendered_image = f"[{self.alt}]({self.filename})"
    return content.replace(self.placeholder, rendered_image)
