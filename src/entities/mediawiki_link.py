import os
import re
from slugify import slugify
from src.dataclasses.content_data import ContentData
from src.lib import fs


MATCHERS = [
    r'^(\[\[([\s\w\d_\-&|]*)\]\])(?:.+)$',
    r'(?!^)(\[\[([\s\w\d_\-&|]*)\]\])',
]


class MediawikiIncludeLink:
    def __init__(self, data: ContentData):
        self.data = data

    def render(self, data):
        content = data.content
        link = f'[{self.data.title}]({self.data.meta.get("link")})'
        not_found = self.data.meta.get('not_found')

        if not_found:
            return content.replace(self.data.placeholder, self.title)

        return content.replace(self.data.placeholder, link)

    @staticmethod
    def get_all(entity):
        if not isinstance(entity.data, ContentData):
            return []

        includes = []
        matches = MediawikiIncludeLink.find_matches(entity.data.content)

        for match in matches:
            placeholder, filename = match
            try:
                filename = filename.split('|')[0].strip()
                filename = fs.find_one_by_glob(f'**/{filename}.md')
                _, meta, _ = fs.load(filename)

                link_url = meta.get('link')
                if not link_url:
                    meta['not_found'] = True
                    print(
                        f'- [LINK NOT FOUND] Link is not defined for {placeholder}'
                    )

                data = ContentData(
                    placeholder=placeholder,
                    filename=filename,
                    meta=meta,
                )

                include = MediawikiIncludeLink(data)

                includes.append(include)
                print(f'- [PARSED]: Link: {placeholder}, {link_url}')
            except Exception as e:
                print(f'- [LINK NOT FOUND] "{placeholder}" {e}')

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

    @staticmethod
    def find_matches(content: str):
        return [
            match
            for r in MATCHERS
            for match in re.findall(r, content, flags=re.MULTILINE)
        ]
