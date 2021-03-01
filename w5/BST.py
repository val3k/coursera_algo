class Node():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BST():
    def __init__(self, root=None):
        self.root = root

    def put(self, key, value):
        self.root = self._put(self.root, key, value)

    def _put(self, node, key, value):
        if node is None:
            return Node(key, value)

        if node.key < key:
            node.right = self._put(node.right, key, value)
        elif node.key > key:
            node.left = self._put(node.left, key, value)
        else:
            node.value = value

        return node

    def get(self, key):
        x = self.root
        while x is not None:
            if key < x.key:
                x = x.left
            elif key > x.key:
                x = x.right
            else:
                return x.value
        return None

    def delete(self, key):
        pass
