import itertools
from src.processors.inline_image import InlineImage
from src.processors.reference_image import ReferenceImage
from src.tree.node import TreeNode

class Page():
  Entities = [InlineImage, ReferenceImage]

  def __init__(self, model):
    self.data = model
    self.head = self.build_tree()
    self.data.entities = self.head.flat()

  def build_tree(self):
    head = TreeNode(self.data)
    head.walk(self.parse_children)
    return head

  def parse_children(self, node):
    print("node", node)
    data = node.data
    entities = map(lambda Entity: Entity.get_all(data), self.Entities)
    flat_entities = list(itertools.chain(*entities))
    nodes = map(TreeNode, flat_entities)
    node.children = nodes

