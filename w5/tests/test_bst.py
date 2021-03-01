from BST import BST, Node


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
