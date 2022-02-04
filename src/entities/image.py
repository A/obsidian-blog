from dataclasses import dataclass
from typing import Optional
from src.dataclasses.image_data import ImageData
from src.entities.entity import EntityInterface
from src.entities.page_data import PageData

@dataclass
class Image(EntityInterface):
  """Basic image class"""
  data: ImageData

  def render(self, entity):
    content = entity.data.content
    rendered_image = f"![{self.data.alt}]({self.data.filename})"
    return content.replace(self.data.placeholder, rendered_image)
