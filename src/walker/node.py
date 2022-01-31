class TreeNode:
  def __init__(self, data):
    self.data = data
    self.children = []

  def walk(self, callback):
    callback(self)
    if not self.children: return
    for child in self.children:
      child.walk(callback)

  def append(self, node):
    self.children.append(node)

  def flat(self):
    nodes = [self]
    if not self.children: return nodes

    for child in self.children:
      nodes = [*nodes, * child.flat()]

    return nodes
