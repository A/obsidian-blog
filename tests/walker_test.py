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
  n0 = TreeNode(data[0])
  n1 = TreeNode(data[1])
  n2 = TreeNode(data[2])
  n3 = TreeNode(data[3])

  n0.append(n1)
  n0.append(n2)
  n2.append(n3)
  
  nodes = n0.flat()

  for (k, _) in enumerate(nodes):
    assert(nodes[k].data == data[k])
