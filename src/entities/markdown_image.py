from marko.ast_renderer import ASTRenderer
from src.dataclasses.content_data import ContentData
from src.dataclasses.asset_data import AssetData
from src.entities.image import Image
from src.entities.parser import get_all_of_types, markdownFabric


class MarkdownImage(Image):
    @classmethod
    def get_all(cls, entity):
        if not isinstance(entity.data, ContentData):
            return []

        imgs = []
        matches = cls.get_matches(entity.data.content)

        for match in matches:
            placeholder, alt, filename = match
            asset_data = AssetData(
                placeholder=placeholder,
                alt=alt,
                filename=filename,
            )
            img = cls(asset_data)
            imgs.append(img)

        return imgs

    @staticmethod
    def get_matches(content):
        print('content', content)
        markdown = markdownFabric(renderer=ASTRenderer)
        ast = markdown(content)
        res = get_all_of_types(['obsidian_embed'], ast)
        breakpoint()
        return res
