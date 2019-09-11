from symmetrical_binary_tree import is_symmetrical_recursion, is_symmetrical
from symmetrical_binary_tree import BinaryTreeNode, connect_binarytree_nodes


def test_full_binary_tree_is():
    #        8
    #    6       6
    #   5 7    7   5
    tree = BinaryTreeNode(8)
    connect_binarytree_nodes(tree, BinaryTreeNode(6), BinaryTreeNode(6))
    connect_binarytree_nodes(tree.left, BinaryTreeNode(5), BinaryTreeNode(7))
    connect_binarytree_nodes(tree.right, BinaryTreeNode(7), BinaryTreeNode(5))
    assert is_symmetrical_recursion(tree) == True
    assert is_symmetrical(tree) == True


def test_full_binary_tree_isnot():
    #        8
    #    6       9
    #   5 7    7   5
    tree = BinaryTreeNode(8)
    connect_binarytree_nodes(tree, BinaryTreeNode(6), BinaryTreeNode(9))
    connect_binarytree_nodes(tree.left, BinaryTreeNode(5), BinaryTreeNode(7))
    connect_binarytree_nodes(tree.right, BinaryTreeNode(7), BinaryTreeNode(5))
    assert is_symmetrical_recursion(tree) == False
    assert is_symmetrical(tree) == False


def test_not_full_binary_tree_isnot():
    #        8
    #    6       6
    #   5 7    7
    tree = BinaryTreeNode(8)
    connect_binarytree_nodes(tree, BinaryTreeNode(6), BinaryTreeNode(6))
    connect_binarytree_nodes(tree.left, BinaryTreeNode(5), BinaryTreeNode(7))
    connect_binarytree_nodes(tree.right, BinaryTreeNode(7), None)
    assert is_symmetrical_recursion(tree) == False
    assert is_symmetrical(tree) == False

def test_not_full_binary_tree_all_nodes_same_isnot():
    #        7
    #    7       7
    #   7 7    7
    tree = BinaryTreeNode(7)
    connect_binarytree_nodes(tree, BinaryTreeNode(7), BinaryTreeNode(7))
    connect_binarytree_nodes(tree.left, BinaryTreeNode(7), BinaryTreeNode(7))
    connect_binarytree_nodes(tree.right, BinaryTreeNode(7), None)
    assert is_symmetrical_recursion(tree) == False
    assert is_symmetrical(tree) == False

def test_special_binary_tree_is():
    #            5
    #          4   4
    #        3       3
    #      2           2
    #    9               9
    tree = BinaryTreeNode(5)
    connect_binarytree_nodes(tree, BinaryTreeNode(4), BinaryTreeNode(4))
    connect_binarytree_nodes(tree.left, BinaryTreeNode(3), None)
    connect_binarytree_nodes(tree.right, None, BinaryTreeNode(3))
    connect_binarytree_nodes(tree.left.left, BinaryTreeNode(2), None)
    connect_binarytree_nodes(tree.right.right, None, BinaryTreeNode(2))
    connect_binarytree_nodes(tree.left.left.left, BinaryTreeNode(9), None)
    connect_binarytree_nodes(tree.right.right.right, None, BinaryTreeNode(9))
    assert is_symmetrical_recursion(tree) == True
    assert is_symmetrical(tree) == True


def test_special_binary_tree_isnot():
    #            5
    #          4   4
    #        3       3
    #      6           2
    #    9               9
    tree = BinaryTreeNode(5)
    connect_binarytree_nodes(tree, BinaryTreeNode(4), BinaryTreeNode(4))
    connect_binarytree_nodes(tree.left, BinaryTreeNode(3), None)
    connect_binarytree_nodes(tree.right, None, BinaryTreeNode(3))
    connect_binarytree_nodes(tree.left.left, BinaryTreeNode(6), None)
    connect_binarytree_nodes(tree.right.right, None, BinaryTreeNode(2))
    connect_binarytree_nodes(tree.left.left.left, BinaryTreeNode(9), None)
    connect_binarytree_nodes(tree.right.right.right, None, BinaryTreeNode(9))
    assert is_symmetrical_recursion(tree) == False
    assert is_symmetrical(tree) == False


def test_special_not_symmetrical_binary_tree_isnot():
    #            5
    #          4   4
    #        3       3
    #      2           2
    #    9
    tree = BinaryTreeNode(5)
    connect_binarytree_nodes(tree, BinaryTreeNode(4), BinaryTreeNode(4))
    connect_binarytree_nodes(tree.left, BinaryTreeNode(3), None)
    connect_binarytree_nodes(tree.right, None, BinaryTreeNode(3))
    connect_binarytree_nodes(tree.left.left, BinaryTreeNode(2), None)
    connect_binarytree_nodes(tree.right.right, None, BinaryTreeNode(2))
    connect_binarytree_nodes(tree.left.left.left, BinaryTreeNode(9), None)
    assert is_symmetrical_recursion(tree) == False
    assert is_symmetrical(tree) == False


def test_special_binary_tree_all_nodes_same_is():
    #            5
    #          5   5
    #        5       5
    #      5           5
    #    5               5
    tree = BinaryTreeNode(5)
    connect_binarytree_nodes(tree, BinaryTreeNode(5), BinaryTreeNode(5))
    connect_binarytree_nodes(tree.left, BinaryTreeNode(5), None)
    connect_binarytree_nodes(tree.right, None, BinaryTreeNode(5))
    connect_binarytree_nodes(tree.left.left, BinaryTreeNode(5), None)
    connect_binarytree_nodes(tree.right.right, None, BinaryTreeNode(5))
    connect_binarytree_nodes(tree.left.left.left, BinaryTreeNode(5), None)
    connect_binarytree_nodes(tree.right.right.right, None, BinaryTreeNode(5))
    assert is_symmetrical_recursion(tree) == True
    assert is_symmetrical(tree) == True


def test_special_not_symmetrical_binary_tree_all_nodes_same_isnot():
    #            5
    #          5   5
    #        5       5
    #      5           5
    #    5           5
    tree = BinaryTreeNode(5)
    connect_binarytree_nodes(tree, BinaryTreeNode(5), BinaryTreeNode(5))
    connect_binarytree_nodes(tree.left, BinaryTreeNode(5), None)
    connect_binarytree_nodes(tree.right, None, BinaryTreeNode(5))
    connect_binarytree_nodes(tree.left.left, BinaryTreeNode(5), None)
    connect_binarytree_nodes(tree.right.right, None, BinaryTreeNode(5))
    connect_binarytree_nodes(tree.left.left.left, BinaryTreeNode(5), None)
    connect_binarytree_nodes(tree.right.right.right, BinaryTreeNode(5), None)
    assert is_symmetrical_recursion(tree) == False
    assert is_symmetrical(tree) == False


def test_one_node():
    tree = BinaryTreeNode(5)
    assert is_symmetrical_recursion(tree) == True
    assert is_symmetrical(tree) == True


def test_none():
    tree = None
    assert is_symmetrical_recursion(tree) == True
    assert is_symmetrical(tree) == True
