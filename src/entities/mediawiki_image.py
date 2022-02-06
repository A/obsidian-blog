import glob
import re
from src.dataclasses.content_data import ContentData
from src.dataclasses.asset_data import AssetData
from src.entities.image import Image


MW_IMG_REGEXP = r'(\!\[\[(.*)\]\])'


class MediawikiImage(Image):
    def __init__(self, data: AssetData):
        self.data = data

    @staticmethod
    def get_all(entity):
        if not isinstance(entity.data, ContentData):
            return []

        imgs = []
        matches = re.findall(MW_IMG_REGEXP, entity.data.content)

        for match in matches:
            placeholder = match[0]
            alt = match[1]

            try:
                filename, *_ = glob.glob(f'**/{alt}', recursive=True)
                data = AssetData(
                    placeholder=placeholder,
                    alt=alt,
                    filename=filename,
                )
                imgs.append(MediawikiImage(data))
                print(f'- [PARSED]: Image: {placeholder}')
            except:
                print(f'- [NOT FOUND] Image "{alt}" not found ')

        return imgs
