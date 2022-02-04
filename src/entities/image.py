from dataclasses import dataclass
from src.dataclasses.image_data import ImageData

@dataclass
class Image():
  """Basic image class"""
  data: ImageData

  def render(self, data):
    content = data.content
    rendered_image = f"![{self.data.alt}]({self.data.filename})"
    return content.replace(self.data.placeholder, rendered_image)
