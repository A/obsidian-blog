import os
from slugify import slugify
from src.dataclasses.content_data import ContentData
from src.entities.parser import get_all_of_types, markdownFabric
from marko.ast_renderer import ASTRenderer
from src.lib import fs


class ObsidianEmbed:
    def __init__(self, data: ContentData):
        self.data = data

    def render(self, data):
        _, ext = os.path.splitext(self.data.filename)

        if ext in ['.png', '.jpg', '.gif']:
            return self.render_image(data)
        if ext in ['.md']:
            return self.render_markdown(data)

    def render_markdown(self, data: ContentData):
        content = data.content
        return content.replace(self.data.placeholder, self.data.content)

    def render_image(self, data: ContentData):
        content = data.content
        template = f'![{self.title}]({self.data.filename})'
        return content.replace(self.data.placeholder, template)

    @staticmethod
    def get_matches(content):
        markdown = markdownFabric(renderer=ASTRenderer)
        ast = markdown(content)
        return get_all_of_types(['obsidian_embed'], ast)

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
                path = fs.find_one_by_glob(f'**/{filename}')
                _, meta, content = fs.load(path)

                data = ContentData(
                    placeholder=placeholder,
                    filename=path,
                    meta=meta,
                    content=content,
                    match=match,
                )

                include = ObsidianEmbed(data)

                includes.append(include)
                print(f'- [PARSED]: Include: {placeholder}')
            except Exception as e:
                print(f'- [NOT FOUND] "{placeholder}" {e}')

        return includes

    @property
    def title(self) -> str:
        if self.data.meta.get('title'):
            return self.data.meta.get('title') or ''
        filename, _ = os.path.splitext(fs.basename(self.data.filename))
        if ' - ' in filename:
            matches = re.findall(r'-(.*)\.\w+$', self.data.filename)
            return matches[0]
        return filename

    @property
    def id(self):
        return slugify(self.title)
