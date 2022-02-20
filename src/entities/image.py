from dataclasses import dataclass
from src.dataclasses.content_data import ContentData


@dataclass
class Image:
    """Basic image class"""

    data: ContentData

    def render(self, data):
        content = data.content
        rendered_image = f'![{self.data.title}]({self.data.filename})'
        return content.replace(self.data.placeholder, rendered_image)
