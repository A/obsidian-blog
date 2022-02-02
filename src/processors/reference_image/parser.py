import re
from src.helpers import normalize_path
from src.models.page import PageModel
from src.processors.reference_image import consts as c
from src.processors.reference_image.entity import ReferenceImageEntity

class ReferenceImageParser():
  key = c.REFERENCE_IMAGE_PARSER_KEY

  def parse(self, data: PageModel):
    reference_images = []

    content = data.content
    matches = re.findall(c.REFERENCE_IMAGE_REGEXP, content)

    for match in matches:
      placeholder, alt, key = match
      link_re = re.compile("\\[" + key + "\\]:\\s(.*)")
      filenames = re.findall(link_re, content)
      refimg = ReferenceImageEntity(
        placeholder, alt, normalize_path(filenames[0]), key, 
      )
      reference_images.append(refimg)

    return reference_images
