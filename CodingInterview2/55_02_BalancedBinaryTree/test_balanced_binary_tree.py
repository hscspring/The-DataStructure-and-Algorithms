from balanced_binary_tree import tree_is_balanced, tree_is_balanced2, tree_is_balanced3
from balanced_binary_tree import BSTNode, connect_bst_nodes


def test_full_binary_tree():
    #        10
    #    6       14
    #   4 8    12   16
    tree = BSTNode(10)
    connect_bst_nodes(tree, BSTNode(6), BSTNode(14))
    connect_bst_nodes(tree.left, BSTNode(4), BSTNode(8))
    connect_bst_nodes(tree.right, BSTNode(12), BSTNode(16))
    assert tree_is_balanced(tree) == True
    assert tree_is_balanced2(tree) == True
    assert tree_is_balanced3(tree) == True


def test_not_full_but_balance_binary_tree():
    #        10
    #     6       14
    #   4   8         16
    #     7
    tree = BSTNode(10)
    connect_bst_nodes(tree, BSTNode(6), BSTNode(14))
    connect_bst_nodes(tree.left, BSTNode(4), BSTNode(8))
    connect_bst_nodes(tree.right, None, BSTNode(16))
    connect_bst_nodes(tree.left.right, BSTNode(7), None)
    assert tree_is_balanced(tree) == True
    assert tree_is_balanced2(tree) == True
    assert tree_is_balanced3(tree) == True


def test_not_balanced_binary_tree1():
    #            1
    #         /      \
    #        2        3
    #       /\
    #      4  5
    #        /
    #       6
    tree = BSTNode(1)
    connect_bst_nodes(tree, BSTNode(2), BSTNode(3))
    connect_bst_nodes(tree.left, BSTNode(4), BSTNode(5))
    connect_bst_nodes(tree.left.right, BSTNode(6), None)
    assert tree_is_balanced(tree) == False
    assert tree_is_balanced2(tree) == False
    assert tree_is_balanced3(tree) == False


def test_not_balanced_binary_tree2():
    #            1
    #         /      \
    #        2        2
    #       /          \
    #      3            3
    #     /              \
    #    4                4
    tree = BSTNode(1)
    connect_bst_nodes(tree, BSTNode(2), BSTNode(2))
    connect_bst_nodes(tree.left, BSTNode(3), None)
    connect_bst_nodes(tree.right, None, BSTNode(3))
    connect_bst_nodes(tree.left.left, BSTNode(4), None)
    connect_bst_nodes(tree.right.right, None, BSTNode(4))
    assert tree_is_balanced(tree) == False
    assert tree_is_balanced2(tree) == False
    assert tree_is_balanced3(tree) == False


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
    assert tree_is_balanced(tree) == False
    assert tree_is_balanced2(tree) == False
    assert tree_is_balanced3(tree) == False


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
    assert tree_is_balanced(tree) == False
    assert tree_is_balanced2(tree) == False
    assert tree_is_balanced3(tree) == False


def test_one_node():
    tree = BSTNode(5)
    assert tree_is_balanced(tree) == True
    assert tree_is_balanced2(tree) == True
    assert tree_is_balanced3(tree) == True


def test_none():
    tree = None
    assert tree_is_balanced(tree) == True
    assert tree_is_balanced2(tree) == True
    assert tree_is_balanced3(tree) == True
    
