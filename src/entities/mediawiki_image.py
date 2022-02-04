import glob
import re
from src.dataclasses.content_data import ContentData
from src.dataclasses.image_data import ImageData
from src.entities.image import Image


MW_IMG_REGEXP = r'(\!\[\[(.*)\]\])'

class MediawikiImage(Image):
  def __init__(self, data: ImageData):
    self.data = data

  @staticmethod
  def get_all(entity):
    if not isinstance(entity.data, ContentData):
      return []

    imgs = []

    content = entity.data.content
    matches = re.findall(MW_IMG_REGEXP, content)

    for match in matches:
      placeholder = match[0]
      alt = match[1]

      try:
        filename, *_ = glob.glob(f"**/{alt}", recursive=True)
        data = ImageData(
          placeholder=placeholder,
          alt=alt,
          filename=filename,
        )
        imgs.append(MediawikiImage(data))
      except:
        print(f"Image \"{alt}\" not found ")

    return imgs
