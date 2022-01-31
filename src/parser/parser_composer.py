class ParserComposer():
  parsers = []

  def __init__(self, parsers):
    self.parsers = parsers

  def parse(self, node):
    return map(lambda p: p.parse(node.data.content), self.parsers)
