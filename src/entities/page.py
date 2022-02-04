import itertools
from src.converters import handlebars, markdown
from src.dataclasses.content_data import ContentData
from src.entities.inline_image import InlineImage
from src.entities.mediawiki_image import MediawikiImage
from src.entities.mediawiki_include import MediawikiInclude
from src.entities.reference_image import ReferenceImage
from src.tree.node import TreeNode


class Page:

  """
  Page is a high-level entity handles building and rendering
  notes graph
  """

  Entities = [InlineImage, ReferenceImage, MediawikiImage, MediawikiInclude]

  def __init__(self, data: ContentData):
    self.data = data
    self.head = self.build_tree()
    self.data.entities = self.head.flat()

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

  # FIXME: if page has render, recursion happens bcz head == page
  def render_self(self, context=None):
    if context == None: context = {}
    content = self.data.content
    if self.data.is_md:
      content = self.render_entities()
      content = markdown.render(content)
    return handlebars.render_template(content, context)

  def render_entities(self):
    for entity in self.data.entities:
      if hasattr(entity.data, "render"):
        self.data.content = entity.data.render(self.data)
    return self.data.content
