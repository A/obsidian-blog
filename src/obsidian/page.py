import os
import itertools
from src.converters import handlebars, markdown
from src.dataclasses.content_data import ContentData
from src.entities.inline_image import InlineImage
from src.entities.mediawiki_image import MediawikiImage
from src.entities.mediawiki_include import MediawikiInclude
from src.entities.mediawiki_link import MediawikiIncludeLink
from src.entities.reference_image import ReferenceImage
from src.lib import fs
from src.tree.node import TreeNode


class Page:

    """
    Page is a high-level entity handles building and rendering
    notes graph
    """

    Entities = [
        InlineImage,
        ReferenceImage,
        MediawikiImage,
        MediawikiInclude,
        MediawikiIncludeLink,
    ]

    def __init__(self, data: ContentData):
        self.data = data
        self.head = self.build_tree()
        self.data.entities = list(
            map(TreeNode.unwrap, self.head.flat_children())
        )

    @staticmethod
    def get_all(pages_dir):
        pages = []

        for file in fs.get_files_in_dir(pages_dir):
            path = os.path.join(pages_dir, file)
            filename, meta, content = fs.load(path)

            content_data = ContentData(
                filename=filename, meta=meta, content=content
            )

            page = Page(content_data)
            pages.append(page)

        return sorted(pages, reverse=True)

    def __lt__(self, other):
        return self.data.date < other.data.date

    def build_tree(self):
        head = TreeNode(self)
        head.walk(self.parse_children)
        return head

    def parse_children(self, node):
        data = node.data
        entities = map(lambda Entity: Entity.get_all(data), self.Entities)
        flat_entities = list(itertools.chain(*entities))
        nodes = list(map(TreeNode, flat_entities))
        node.children = nodes

    def render(self, context=None):
        if context == None:
            context = {}
        content = self.data.content
        if self.data.ext == '.md':
            content = self.render_entities()
            content = markdown.render(content)
        try:
            return handlebars.render_template(content, context)
        except:
            return content

    def render_entities(self):
        for entity in self.data.entities:
            if hasattr(entity, 'render'):
                data = entity.data
                if hasattr(data, 'is_private') and data.is_private:
                    if data.content != '':
                        print(data.content)
                        print(
                            f'  - [SKIP]: {data.placeholder} is private, add `published: True` attribute to the frontmetter to publish it'
                        )
                        continue
                self.data.content = entity.render(self.data)
        return self.data.content
