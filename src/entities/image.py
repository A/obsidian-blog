from dataclasses import dataclass
from src.dataclasses.asset_data import AssetData


@dataclass
class Image:
    """Basic image class"""

    data: AssetData

    def render(self, data):
        content = data.content
        rendered_image = f'![{self.data.alt}]({self.data.filename})'
        return content.replace(self.data.placeholder, rendered_image)
