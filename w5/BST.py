class Node():
    def __init__(self, key, value, color):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.color = color
        self.cnt = 1


class BST():
    def __init__(self, root=None):
        self.root = root

    def put(self, key, value):
        self.root = self._put(self.root, key, value)

    def _put(self, node, key, value):
        if node is None:
            return Node(key, value, 'RED')

        if node.key < key:
            node.right = self._put(node.right, key, value)
        elif node.key > key:
            node.left = self._put(node.left, key, value)
        else:
            node.value = value

        if self.is_red(node.right) and not self.is_red(node.left):
            node = self.rotate_left(node)
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)
        if self.is_red(node.left) and self.is_red(node.right):
            self.flip_color(node)
        node.cnt = 1 + self.size(node.left) + self.size(node.right)
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

    def inorder(self):
        ord_list = []
        self._inorder(self.root, ord_list)
        return ord_list

    def _inorder(self, node, ord_list):
        if node is None:
            return
        self._inorder(node.left, ord_list)
        ord_list.append(node.key)
        self._inorder(node.right, ord_list)

    def is_red(self, node):
        if node is None:
            return False
        return node.color == 'RED'

    def rotate_left(self, node):
        roteted = node.right
        node.right = roteted.left
        roteted.left = node
        roteted.color = node.color
        node.color = 'RED'
        node.cnt = 1 + self.size(node.left) + self.size(node.right)
        return roteted

    def rotate_right(self, node):
        roteted = node.left
        node.left = roteted.right
        roteted.right = node
        roteted.color = node.color
        node.color = 'RED'
        node.cnt = 1 + self.size(node.left) + self.size(node.right)
        return roteted

    def flip_color(self, node):
        node.color = 'RED'
        node.left.color = 'BLACK'
        node.right.color = 'BLACK'

    def size(self, node):
        if node is None:
            return 0
        else:
            return node.cnt

    def rank(self, key, node=None):
        if node is None:
            node = self.root
        if key == node.key:
            return self.size(node.left)
        elif key > node.key:
            return 1 + self.size(node.left) + self.rank(key, node.right)
        else:
            return self.rank(key, node.left)

    def range_count(self, low_key, hi_key):
        if self.get(hi_key) is not None:
            return self.rank(hi_key) - self.rank(low_key) + 1
        else:
            return self.rank(hi_key) - self.rank(low_key)

    def range_search(self, low_key, hi_key, node=None, search_res=[]):
        if node is None:
            node = self.root

        if node.key > low_key:
            search_res = self.range_search(low_key, hi_key, node=node.left, search_res=search_res)
        elif low_key <= node.key <= hi_key:
            search_res.append(node.key)
            return search_res
        if node.key < hi_key:
            search_res = self.range_search(low_key, hi_key, node=node.right, search_res=search_res)
        elif low_key <= node.key <= hi_key:
            search_res.append(node.key)
            return search_res
        
        return search_res

            

        


