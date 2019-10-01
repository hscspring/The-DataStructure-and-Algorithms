from kth_node_in_bst import kth_node
from kth_node_in_bst import BSTNode, connect_bst_nodes


def test_full_binary_tree():
    #        10
    #    6       14
    #   4 8    12   16
    tree = BSTNode(10)
    connect_bst_nodes(tree, BSTNode(6), BSTNode(14))
    connect_bst_nodes(tree.left, BSTNode(4), BSTNode(8))
    connect_bst_nodes(tree.right, BSTNode(12), BSTNode(16))
    assert kth_node(tree, 0) == -1
    assert kth_node(tree, 1) == 4
    assert kth_node(tree, 2) == 6
    assert kth_node(tree, 3) == 8
    assert kth_node(tree, 4) == 10
    assert kth_node(tree, 5) == 12
    assert kth_node(tree, 6) == 14
    assert kth_node(tree, 7) == 16
    assert kth_node(tree, 8) == -1


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
    assert kth_node(tree, 0) == -1
    assert kth_node(tree, 1) == 1
    assert kth_node(tree, 2) == 2
    assert kth_node(tree, 3) == 3
    assert kth_node(tree, 4) == 4
    assert kth_node(tree, 5) == 5
    assert kth_node(tree, 6) == -1


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
    assert kth_node(tree, 0) == -1
    assert kth_node(tree, 1) == 1
    assert kth_node(tree, 2) == 2
    assert kth_node(tree, 3) == 3
    assert kth_node(tree, 4) == 4
    assert kth_node(tree, 5) == 5
    assert kth_node(tree, 6) == -1


def test_one_node():
    tree = BSTNode(5)
    assert kth_node(tree, 0) == -1
    assert kth_node(tree, 1) == 5
    assert kth_node(tree, 2) == -1


def test_none():
    tree = None
    assert kth_node(tree, 0) == -1
    assert kth_node(tree, 1) == -1
