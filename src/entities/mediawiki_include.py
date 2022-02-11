import os
import re
from slugify import slugify
from src.dataclasses.content_data import ContentData
from src.lib import fs


MW_INCLUDE_REGEXP = r'^(\[\[([\s\w\d_\-&|]*)\]\])$'


class MediawikiInclude:
    def __init__(self, data: ContentData):
        self.data = data

    @staticmethod
    def get_all(entity):
        if not isinstance(entity.data, ContentData):
            return []

        includes = []
        matches = re.findall(
            MW_INCLUDE_REGEXP, entity.data.content, flags=re.MULTILINE
        )

        for match in matches:
            placeholder, filename = match
            try:
                filename = fs.find_one_by_glob(f'**/{filename}.md')
                _, meta, content = fs.load(filename)

                data = ContentData(
                    placeholder=placeholder,
                    filename=filename,
                    meta=meta,
                    content=content,
                )

                include = MediawikiInclude(data)

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

    def render(self, data):
        content = data.content
        return content.replace(self.data.placeholder, self.data.content)
