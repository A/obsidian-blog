class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def walk(self, callback):
        callback(self)
        if not self.children:
            return
        for child in self.children:
            child.walk(callback)

    def append(self, node):
        self.children.append(node)

    def flat(self, visited=None):
        if visited == None:
            visited = []
        if self in visited:
            return visited

        visited.append(self)
        for child in self.children:
            child.flat(visited)

        return visited

    def flat_children(self):
        entities = self.flat()
        del entities[0]
        return entities

    @staticmethod
    def unwrap(node: 'TreeNode'):
        return node.data
