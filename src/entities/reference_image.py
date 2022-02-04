import re
from src.dataclasses.content_data import ContentData
from src.dataclasses.image_data import ImageData
from src.entities.content_entity import ContentEntityInterface
from src.entities.entity import EntityInterface
from src.entities.image import Image
from src.helpers import normalize_path

REFERENCE_IMG_RE = r'(\!\[(.*)]\[(.*)\])'

class ReferenceImage(Image):

  @staticmethod
  def get_all(entity):
    """parse all reference image entities from a given page model"""
    if not isinstance(entity.data, ContentData):
      return []

    imgs = []
    content = entity.data.content
    matches = re.findall(REFERENCE_IMG_RE, content)

    for match in matches:
      placeholder, alt, key = match
      link_re = re.compile("\\[" + key + "\\]:\\s(.*)")
      filename = re.findall(link_re, content)[0]

      data = ImageData(
        placeholder=placeholder,
        alt=alt,
        filename=normalize_path(filename),
        key=key, 
      )
      imgs.append(ReferenceImage(data=data))

    return imgs
