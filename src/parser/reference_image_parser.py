import re
from src.helpers import normalize_path
from src.models.page import PageModel

PARSER_KEY = "reference-image-entity"
REFERENCE_IMAGE_REGEXP = r'(\!\[(.*)]\[(.*)\])'

class ReferenceImageEntry:
  parser_key = PARSER_KEY

  def __init__(self, placeholder, alt, filename, key):
    self.placeholder = placeholder
    self.alt = alt
    self.key = key
    self.filename = filename

class ReferenceImageParser():
  key = PARSER_KEY

  def parse(self, data: PageModel):
    reference_images = []

    content = data.content
    matches = re.findall(REFERENCE_IMAGE_REGEXP, content)

    for match in matches:
      placeholder, alt, key = match
      link_re = re.compile("\\[" + key + "\\]:\\s(.*)")
      filenames = re.findall(link_re, content)
      refimg = ReferenceImageEntry(
        placeholder, alt, normalize_path(filenames[0]), key, 
      )
      reference_images.append(refimg)

    return reference_images
