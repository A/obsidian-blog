import re
from src.dataclasses.content_data import ContentData
from src.dataclasses.asset_data import AssetData
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
            asset_data = AssetData(
                placeholder=placeholder,
                alt=alt,
                filename=filename,
            )
            img = InlineImage(asset_data)
            imgs.append(img)

        return imgs
