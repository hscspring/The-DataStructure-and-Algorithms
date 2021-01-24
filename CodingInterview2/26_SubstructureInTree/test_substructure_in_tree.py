from substructure_in_tree import has_subtree, BinaryTreeNode
from substructure_in_tree import connect_binarytree_nodes


def test_has_branch_is_sub():
    #           8
    #       8      7
    #     9   2
    #       4   7

    #   8
    # 9   2

    tree = BinaryTreeNode(8)
    connect_binarytree_nodes(tree, BinaryTreeNode(8), BinaryTreeNode(7))
    connect_binarytree_nodes(tree.left, BinaryTreeNode(9), BinaryTreeNode(2))
    connect_binarytree_nodes(
        tree.left.right, BinaryTreeNode(4), BinaryTreeNode(7))

    subtree = BinaryTreeNode(8)
    connect_binarytree_nodes(subtree, BinaryTreeNode(9), BinaryTreeNode(2))

    assert has_subtree(tree, subtree) == True


def test_has_branch_isnot_sub():
    #           8
    #       8      7
    #     9   3
    #       4   7

    #   8
    # 9   2

    tree = BinaryTreeNode(8)
    connect_binarytree_nodes(tree, BinaryTreeNode(8), BinaryTreeNode(7))
    connect_binarytree_nodes(tree.left, BinaryTreeNode(9), BinaryTreeNode(3))
    connect_binarytree_nodes(
        tree.left.right, BinaryTreeNode(4), BinaryTreeNode(7))

    subtree = BinaryTreeNode(8)
    connect_binarytree_nodes(subtree, BinaryTreeNode(9), BinaryTreeNode(2))

    assert has_subtree(tree, subtree) == False


def test_left_is_sub():
    #            5
    #          4
    #        3
    #      2
    #    9

    #        4
    #      3
    #    2

    tree = BinaryTreeNode(5)
    connect_binarytree_nodes(tree, BinaryTreeNode(4), None)
    connect_binarytree_nodes(tree.left, BinaryTreeNode(3), None)
    connect_binarytree_nodes(tree.left.left, BinaryTreeNode(2), None)
    connect_binarytree_nodes(tree.left.left.left, BinaryTreeNode(9), None)

    subtree = BinaryTreeNode(4)
    connect_binarytree_nodes(subtree, BinaryTreeNode(3), None)
    connect_binarytree_nodes(subtree.left, BinaryTreeNode(2), None)

    assert has_subtree(tree, subtree) == True


def test_left_isnot_sub():
    #            5
    #          4
    #        3
    #      2
    #    9

    #        4
    #      3
    #    3

    tree = BinaryTreeNode(5)
    connect_binarytree_nodes(tree, BinaryTreeNode(4), None)
    connect_binarytree_nodes(tree.left, BinaryTreeNode(3), None)
    connect_binarytree_nodes(tree.left.left, BinaryTreeNode(2), None)
    connect_binarytree_nodes(tree.left.left.left, BinaryTreeNode(9), None)

    subtree = BinaryTreeNode(4)
    connect_binarytree_nodes(subtree, BinaryTreeNode(3), None)
    connect_binarytree_nodes(subtree.left, BinaryTreeNode(3), None)

    assert has_subtree(tree, subtree) == False


def test_right_is_sub():
    #   5
    #      4
    #         3
    #            2
    #               9

    #   4
    #      3
    #        2

    tree = BinaryTreeNode(5)
    connect_binarytree_nodes(tree, None, BinaryTreeNode(4))
    connect_binarytree_nodes(tree.right, None, BinaryTreeNode(3))
    connect_binarytree_nodes(tree.right.right, None, BinaryTreeNode(2))
    connect_binarytree_nodes(tree.right.right.right, None, BinaryTreeNode(9))

    subtree = BinaryTreeNode(4)
    connect_binarytree_nodes(subtree, None, BinaryTreeNode(3))
    connect_binarytree_nodes(subtree.right, None, BinaryTreeNode(2))

    assert has_subtree(tree, subtree) == True


def test_right_isnot_sub():
    #   5
    #      4
    #         3
    #            2
    #               9

    #   4
    #      3
    #        3

    tree = BinaryTreeNode(5)
    connect_binarytree_nodes(tree, None, BinaryTreeNode(4))
    connect_binarytree_nodes(tree.right, None, BinaryTreeNode(3))
    connect_binarytree_nodes(tree.right.right, None, BinaryTreeNode(2))
    connect_binarytree_nodes(tree.right.right.right, None, BinaryTreeNode(9))

    subtree = BinaryTreeNode(4)
    connect_binarytree_nodes(subtree, None, BinaryTreeNode(3))
    connect_binarytree_nodes(subtree.right, None, BinaryTreeNode(3))

    assert has_subtree(tree, subtree) == False


def test_tree_none_subtree_not():
    tree = None

    subtree = BinaryTreeNode(8)
    connect_binarytree_nodes(subtree, BinaryTreeNode(9), BinaryTreeNode(2))

    assert has_subtree(tree, subtree) == False


def test_subtree_none_tree_not():
    tree = BinaryTreeNode(8)
    connect_binarytree_nodes(tree, BinaryTreeNode(9), BinaryTreeNode(2))

    subtree = None
    assert has_subtree(tree, subtree) == False


def test_none():
    tree = None
    subtree = None
    assert has_subtree(tree, subtree) == False
