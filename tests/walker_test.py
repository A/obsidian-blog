from src.walker.node import TreeNode

def test_tree_node():
  data = "head node"
  head = TreeNode(data)
  assert(head.data == data)

def test_tree_node_append():
  data = range(2)
  head = TreeNode(data[0])
  node = TreeNode(data[1])
  head.append(node)
  
  nodes = []
  head.walk(lambda n: nodes.append(n))

  for (k, _) in enumerate(nodes):
    assert(nodes[k].data == data[k])


def test_signle_tree_node_flat():
  data = range(2)

  head = TreeNode(data[0])
  nodes = head.flat()

  assert(nodes[0].data == data[0])


def test_tree_node_flat():
  data = range(4)
  nodes = []
  for v in data:
    nodes.append(TreeNode(v))

  head = nodes[0]
  nodes[0].append(nodes[1])
  nodes[0].append(nodes[2])
  nodes[2].append(nodes[3])
  
  for (k, node) in enumerate(head.flat()):
    assert(node.data == data[k])

def test_tree_node_recursive_flat():
  data = range(4)
  nodes = []
  for v in data: nodes.append(TreeNode(v))

  head = nodes[0]
  nodes[0].append(nodes[1])
  nodes[0].append(nodes[2])
  nodes[2].append(nodes[3])
  nodes[2].append(nodes[0])

  for (k, node) in enumerate(head.flat()):
    assert(node.data == data[k])
