from serialize_binary_trees import serialize, deserialize
from serialize_binary_trees import BinaryTreeNode, connect_binarytree_nodes, travel_preorder


def test_full_binary_tree():
    #        8
    #    6       10
    #   5 7    9    11
    tree = BinaryTreeNode(8)
    connect_binarytree_nodes(tree, BinaryTreeNode(6), BinaryTreeNode(10))
    connect_binarytree_nodes(tree.left, BinaryTreeNode(5), BinaryTreeNode(7))
    connect_binarytree_nodes(tree.right, BinaryTreeNode(9), BinaryTreeNode(11))
    res = serialize(tree, [])
    head = deserialize(res.copy())
    assert travel_preorder(head, []) == res


def test_left_binary_tree():
    #            5
    #          4
    #        3
    #      2
    #    9
    tree = BinaryTreeNode(5)
    connect_binarytree_nodes(tree, BinaryTreeNode(4), None)
    connect_binarytree_nodes(tree.left, BinaryTreeNode(3), None)
    connect_binarytree_nodes(tree.left.left, BinaryTreeNode(2), None)
    connect_binarytree_nodes(tree.left.left.left, BinaryTreeNode(9), None)
    res = serialize(tree, [])
    head = deserialize(res.copy())
    assert travel_preorder(head, []) == res

def test_right_binary_tree():
    #   5
    #      4
    #         3
    #            2
    #               9
    tree = BinaryTreeNode(5)
    connect_binarytree_nodes(tree, None, BinaryTreeNode(4))
    connect_binarytree_nodes(tree.right, None, BinaryTreeNode(3))
    connect_binarytree_nodes(tree.right.right, None, BinaryTreeNode(2))
    connect_binarytree_nodes(tree.right.right.right, None, BinaryTreeNode(9))
    res = serialize(tree, [])
    head = deserialize(res.copy())
    assert travel_preorder(head, []) == res


def test_complex_binary_tree():
    #        5
    #         5
    #          5
    #         5
    #        5
    #       5 5
    #      5   5
    tree = BinaryTreeNode(5)
    connect_binarytree_nodes(tree, None, BinaryTreeNode(5))
    connect_binarytree_nodes(tree.right, None, BinaryTreeNode(5))
    connect_binarytree_nodes(tree.right.right, BinaryTreeNode(5), None)
    connect_binarytree_nodes(tree.right.right.left, BinaryTreeNode(5), None)
    connect_binarytree_nodes(tree.right.right.left.left, BinaryTreeNode(5), BinaryTreeNode(5))
    connect_binarytree_nodes(tree.right.right.left.left.left, BinaryTreeNode(5), None)
    connect_binarytree_nodes(tree.right.right.left.left.right, None, BinaryTreeNode(5))
    res = serialize(tree, [])
    head = deserialize(res.copy())
    assert travel_preorder(head, []) == res


def test_one_node():
    tree = BinaryTreeNode(5)
    res = serialize(tree, [])
    head = deserialize(res.copy())
    assert travel_preorder(head, []) == res


def test_none():
    tree = None
    res = serialize(tree, [])
    head = deserialize(res.copy())
    assert travel_preorder(head, []) == res




