import itertools
from src.models.page import PageModel
from src.walker.node import TreeNode
from src.parser.parser_composer import ParserComposer
from src.parser.footnote_parser import FootnoteParser
from src.parser.inline_image_parser import InlineImageParser
from src.parser.internal_link_parser import InternalLinkParser
from src.parser.mediawiki_image_parser import MediaWikiImageParser
from src.parser.reference_image_parser import ReferenceImageParser

PAGE_PARSERS = [
    # FootnoteParser(),
    # InternalLinkParser(),
    # InlineImageParser(),
    # MediaWikiImageParser(),
    # ReferenceImageParser(),
]

class PageBuilder():
  def __init__(self, model, parser):
    self.parser = parser
    self.data = model
    self.head = self.build_tree()
    self.data.entities = self.get_entities()

  def get_entities(self):
    return list(itertools.groupby(
      TreeNode.flat(self.head),
      lambda node: PageModel(node.data).filename
    ))

  def build_tree(self):
    node = TreeNode(self.data)
    node.walk(self.parse_children)
    return node

  def parse_children(self, node):
    data = node.data
    entities = self.parser.parse(data.content)
    nodes = map(TreeNode, entities)
    node.children = nodes

