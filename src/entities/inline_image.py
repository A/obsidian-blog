import re
from src.dataclasses.content_data import ContentData
from src.dataclasses.asset_data import AssetData
from src.entities.image import Image

INLINE_IMG_RE = r'(\!\[(.*?)\]\((.*?)\))'


class InlineImage(Image):
    @classmethod
    def get_all(cls, entity):
        if not isinstance(entity.data, ContentData):
            return []

        if entity.data.ext is '.md':
            return []

        imgs = []
        matches = re.findall(INLINE_IMG_RE, entity.data.content)

        for match in matches:
            placeholder, _, filename = match
            image = ContentData(
                placeholder=placeholder,
                filename=filename,
            )
            img = cls(image)
            imgs.append(img)

        return imgs
