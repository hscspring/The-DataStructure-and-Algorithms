from tree_depth import tree_depth
from tree_depth import BSTNode, connect_bst_nodes


def test_binary_tree():
    #        10
    #    6       14
    #   4 8         16
    #    7
    tree = BSTNode(10)
    connect_bst_nodes(tree, BSTNode(6), BSTNode(14))
    connect_bst_nodes(tree.left, BSTNode(4), BSTNode(8))
    connect_bst_nodes(tree.right, None, BSTNode(16))
    connect_bst_nodes(tree.left.right, BSTNode(7), None)
    assert tree_depth(tree) == 4


def test_left_binary_tree():
    #            5
    #          4
    #        3
    #      2
    #    1
    tree = BSTNode(5)
    connect_bst_nodes(tree, BSTNode(4), None)
    connect_bst_nodes(tree.left, BSTNode(3), None)
    connect_bst_nodes(tree.left.left, BSTNode(2), None)
    connect_bst_nodes(tree.left.left.left, BSTNode(1), None)
    assert tree_depth(tree) == 5


def test_right_binary_tree():
    #   1
    #      2
    #         3
    #            4
    #               5
    tree = BSTNode(1)
    connect_bst_nodes(tree, None, BSTNode(2))
    connect_bst_nodes(tree.right, None, BSTNode(3))
    connect_bst_nodes(tree.right.right, None, BSTNode(4))
    connect_bst_nodes(tree.right.right.right, None, BSTNode(5))
    assert tree_depth(tree) == 5


def test_one_node():
    tree = BSTNode(5)
    assert tree_depth(tree) == 1


def test_none():
    tree = None
    assert tree_depth(tree) == 0
