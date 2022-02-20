import os
from slugify import slugify
from src.dataclasses.content_data import ContentData
from src.entities.parser import get_all_of_types, markdownFabric
from marko.ast_renderer import ASTRenderer
from src.lib import fs


class ObsidianLink:
    def __init__(self, data: ContentData):
        self.data = data

    @property
    def title(self) -> str:
        return self.data.title

    @property
    def id(self):
        return slugify(self.title)

    @staticmethod
    def get_matches(content):
        markdown = markdownFabric(renderer=ASTRenderer)
        ast = markdown(content)
        return get_all_of_types(['obsidian_link'], ast)

    def render(self, data):
        content = data.content
        not_found = self.data.meta.get('not_found')

        if not_found:
            return content.replace(self.data.placeholder, self.title)

        link = f'[{self.data.title}]({self.data.meta.get("link")})'
        return content.replace(self.data.placeholder, link)

    @classmethod
    def get_all(cls, entity):
        if not isinstance(entity.data, ContentData):
            return []

        includes = []
        matches = cls.get_matches(entity.data.content)

        for match in matches:
            placeholder = match['placeholder']
            target = match['target']

            # TODO: Duplication
            filename = target
            _, ext = os.path.splitext(filename)

            if ext:
                filename = target
            else:
                filename = f'{target}.md'

            try:
                _, ext = os.path.splitext(filename)

                if ext != '.md':
                    continue

                filename = fs.find_one_by_glob(f'**/{filename}')
                _, meta, _ = fs.load(filename)

                url = meta.get('link')
                if not url:
                    meta['not_found'] = True
                    print(
                        f'- [LINK NOT FOUND] Link is not defined for {placeholder}'
                    )

                data = ContentData(
                    placeholder=placeholder,
                    filename=filename,
                    meta=meta,
                    match=match,
                )

                include = cls(data)
                includes.append(include)

                print(f'- [PARSED]: Link: {placeholder}, {url}')
            except Exception as e:
                print(f'- [LINK NOT FOUND] "{placeholder}" {e}')

        return includes
