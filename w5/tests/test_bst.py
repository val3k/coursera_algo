from BST import BST, Node
from kdtree import PointSet, Point


def test_get():
    root = Node('b', 5)
    root.left = Node('a', 3)
    root.right = Node('c', 2)
    bst = BST(root)

    assert bst.get('a') == 3
    assert bst.get('c') == 2
    assert bst.get('d') is None


def test_put():
    bst = BST()
    bst.put('c', 3)
    assert bst.root.value == 3

    bst.put('b', 5)
    assert bst.root.left.value == 5
    bst.put('a', 1)
    assert bst.root.left.left.value == 1
    bst.put('d', 4)
    assert bst.root.right.value == 4
    bst.put('f', 7)
    assert bst.root.right.right.value == 7


def test_order():
    bst = BST()
    bst.put('s', 3)

    bst.put('e', 5)
    bst.put('a', 1)
    bst.put('x', 0)

    bst.put('r', 4)
    bst.put('h', 7)
    a = bst.inorder()
    assert a == ['a', 'e', 'h', 'r', 's', 'x']


def test_rb_tree():
    bst = BST()
    bst.put('a', 1)
    bst.put('b', 1)
    bst.put('c', 1)
    bst.put('d', 1)
    bst.put('e', 1)

    assert bst.root.key == 'd'
    assert bst.root.left.key == 'b'
    a = bst.inorder()
    assert a == ['a', 'b', 'c', 'd', 'e']


def test_size():
    bst = BST()
    bst.put('a', 1)
    assert bst.root.cnt == 1
    bst.put('b', 1)
    assert bst.root.cnt == 2
    bst.put('c', 1)
    assert bst.root.cnt == 3
    bst.put('d', 1)
    assert bst.root.cnt == 4
    bst.put('e', 1)
    assert bst.root.cnt == 5


def test_rank():
    bst = BST()
    bst.put('a', 1)
    bst.put('b', 1)
    bst.put('c', 1)
    bst.put('d', 1)
    bst.put('e', 1)
    assert bst.rank('c') == 2
    assert bst.rank('b') == 1
    assert bst.rank('d') == 3
    assert bst.rank('e') == 4


def test_range_count():
    bst = BST()
    bst.put('a', 1)
    bst.put('b', 1)
    bst.put('c', 1)
    bst.put('d', 1)
    bst.put('e', 1)
    assert bst.range_count('b', 'e') == 4


def test_range_search():
    bst = BST()
    bst.put('a', 1)
    bst.put('b', 1)
    bst.put('c', 1)
    bst.put('d', 1)
    bst.put('e', 1)

    assert bst.range_search('b', 'd') == ['b', 'c', 'd']


def test_point_tree():
    ps = PointSet()
    p1 = Point(1, 1)
    ps.insert(p1)
    assert ps.contains(p1)
