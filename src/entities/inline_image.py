import re
from src.dataclasses.content_data import ContentData
from src.dataclasses.image_data import ImageData
from src.entities.image import Image

INLINE_IMG_RE = r'(\!\[(.*)\]\((.*)\))'

class InlineImage(Image):

  @staticmethod
  def get_all(entity):
    if not isinstance(entity.data, ContentData):
      return []

    imgs = []
    matches = re.findall(INLINE_IMG_RE, entity.data.content)

    for match in matches:
      placeholder, alt, filename = match
      image_data = ImageData(
        placeholder=placeholder,
        alt=alt,
        filename=filename,
      )
      img = InlineImage(image_data)
      imgs.append(img)

    return imgs
