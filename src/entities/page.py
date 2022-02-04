import itertools
from src import handlebars, markdown
from src.entities.inline_image import InlineImage
from src.entities.page_data import PageData
from src.entities.reference_image import ReferenceImage
from src.tree.node import TreeNode


class Page:
  Entities = [InlineImage, ReferenceImage]

  def __init__(self, data: PageData):
    self.data = data
    self.head = self.build_tree()
    self.data.entities = self.head.flat()

  def build_tree(self):
    head = TreeNode(self.data)
    head.walk(self.parse_children)
    return head

  def parse_children(self, node):
    data = node.data
    entities = map(lambda Entity: Entity.get_all(data), self.Entities)
    flat_entities = list(itertools.chain(*entities))
    nodes = map(TreeNode, flat_entities)
    node.children = nodes

  def render(self, context):
    content = self.data.content
    if self.data.is_md:
      content = self.render_entities()
      content = markdown.render(content)
    return handlebars.render_template(content, context)

  def render_entities(self):
    content = self.data.content
    for entity in self.data.entities:
      if hasattr(entity.data, "render"):
        content = entity.data.render(self.data)
    return content
