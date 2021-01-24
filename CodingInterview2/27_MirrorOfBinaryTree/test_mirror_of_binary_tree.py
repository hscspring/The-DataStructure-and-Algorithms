from mirror_of_binary_tree import mirror_recursion, mirror
from mirror_of_binary_tree import BinaryTreeNode, connect_binarytree_nodes

def test_full_binary_tree():
    #        8
    #    6      10
    #   5 7    9  11
    tree = BinaryTreeNode(8)
    connect_binarytree_nodes(tree, BinaryTreeNode(6), BinaryTreeNode(10))
    connect_binarytree_nodes(tree.left, BinaryTreeNode(5), BinaryTreeNode(7))
    connect_binarytree_nodes(tree.right, BinaryTreeNode(9), BinaryTreeNode(11))
    mtree = mirror_recursion(tree)
    assert mtree.left.val == 10
    assert mtree.right.left.val == 7
    
    tree = BinaryTreeNode(8)
    connect_binarytree_nodes(tree, BinaryTreeNode(6), BinaryTreeNode(10))
    connect_binarytree_nodes(tree.left, BinaryTreeNode(5), BinaryTreeNode(7))
    connect_binarytree_nodes(tree.right, BinaryTreeNode(9), BinaryTreeNode(11))
    mtree = mirror(tree)
    assert mtree.left.val == 10
    assert mtree.right.left.val == 7

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
    mtree = mirror_recursion(tree)
    assert mtree.right.val == 4
    assert mtree.right.right.val == 3

    tree = BinaryTreeNode(5)
    connect_binarytree_nodes(tree, BinaryTreeNode(4), None)
    connect_binarytree_nodes(tree.left, BinaryTreeNode(3), None)
    connect_binarytree_nodes(tree.left.left, BinaryTreeNode(2), None)
    connect_binarytree_nodes(tree.left.left.left, BinaryTreeNode(9), None)
    mtree = mirror(tree)
    assert mtree.right.val == 4
    assert mtree.right.right.val == 3

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
    mtree = mirror_recursion(tree)
    assert mtree.left.val == 4
    assert mtree.left.left.val == 3

    tree = BinaryTreeNode(5)
    connect_binarytree_nodes(tree, None, BinaryTreeNode(4))
    connect_binarytree_nodes(tree.right, None, BinaryTreeNode(3))
    connect_binarytree_nodes(tree.right.right, None, BinaryTreeNode(2))
    connect_binarytree_nodes(tree.right.right.right, None, BinaryTreeNode(9))
    mtree = mirror(tree)
    assert mtree.left.val == 4
    assert mtree.left.left.val == 3


def test_one_node():
    tree = BinaryTreeNode(5)
    mtree = mirror_recursion(tree)
    assert mtree.left == None

    tree = BinaryTreeNode(5)
    mtree = mirror(tree)
    assert mtree.left == None

def test_none():
    tree = None
    mtree = mirror_recursion(tree)
    assert mtree == None

    tree = None
    mtree = mirror(tree)
    assert mtree == None




