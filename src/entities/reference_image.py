import re
from src.helpers import normalize_path
from src.models.page import PageModel

REFERENCE_IMG_RE = r'(\!\[(.*)]\[(.*)\])'

class ReferenceImage:

  def __init__(self, placeholder, alt, filename, key):
    self.placeholder = placeholder
    self.alt = alt
    self.key = key
    self.filename = filename

  @staticmethod
  def get_all(data: PageModel):
    """parse all reference image entities from a given page model"""
    if not hasattr(data, "content"): return []

    reference_images = []
    content = data.content
    matches = re.findall(REFERENCE_IMG_RE, content)

    for match in matches:
      placeholder, alt, key = match
      link_re = re.compile("\\[" + key + "\\]:\\s(.*)")
      filenames = re.findall(link_re, content)
      refimg = ReferenceImage(
        placeholder, alt, normalize_path(filenames[0]), key, 
      )
      reference_images.append(refimg)

    return reference_images
  
  @staticmethod
  def render_one(data: PageModel, entity: "ReferenceImage"):
    if not isinstance(entity, ReferenceImage): return
    rendered_image = f"![{entity.alt}]({entity.filename})"
    return data.content.replace(entity.placeholder, rendered_image)
