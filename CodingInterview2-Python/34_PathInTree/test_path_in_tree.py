from path_in_tree import find_path
from path_in_tree import BinaryTreeNode, connect_binarytree_nodes


def test_full_binary_tree():
    #        8
    #    1       2
    #   3 4    7   3
    tree = BinaryTreeNode(8)
    connect_binarytree_nodes(tree, BinaryTreeNode(1), BinaryTreeNode(2))
    connect_binarytree_nodes(tree.left, BinaryTreeNode(3), BinaryTreeNode(4))
    connect_binarytree_nodes(tree.right, BinaryTreeNode(7), BinaryTreeNode(3))
    assert find_path(tree, 13) == [[8,1,4],[8,2,3]]
    assert find_path(tree, 12) == [[8,1,3]]
    assert find_path(tree, 11) == []


def test_not_full_binary_tree():
    #        8
    #    1       2
    #   5 3    7
    tree = BinaryTreeNode(8)
    connect_binarytree_nodes(tree, BinaryTreeNode(1), BinaryTreeNode(2))
    connect_binarytree_nodes(tree.left, BinaryTreeNode(5), BinaryTreeNode(3))
    connect_binarytree_nodes(tree.right, BinaryTreeNode(7), None)
    assert find_path(tree, 17) == [[8,2,7]]
    assert find_path(tree, 16) == []


def test_not_full_binary_tree_simple():
    #        1
    #    3      
    #       2    
    tree = BinaryTreeNode(1)
    connect_binarytree_nodes(tree, BinaryTreeNode(3), None)
    connect_binarytree_nodes(tree.left, None, BinaryTreeNode(2))
    assert find_path(tree, 6) == [[1,3,2]]
    assert find_path(tree, 5) == []
    assert find_path(tree, 9) == []


def test_special_binary_tree():
    #            5
    #          1   4
    #        2       3
    #      7           2
    #    8               9
    tree = BinaryTreeNode(5)
    connect_binarytree_nodes(tree, BinaryTreeNode(1), BinaryTreeNode(4))
    connect_binarytree_nodes(tree.left, BinaryTreeNode(2), None)
    connect_binarytree_nodes(tree.right, None, BinaryTreeNode(3))
    connect_binarytree_nodes(tree.left.left, BinaryTreeNode(7), None)
    connect_binarytree_nodes(tree.right.right, None, BinaryTreeNode(2))
    connect_binarytree_nodes(tree.left.left.left, BinaryTreeNode(8), None)
    connect_binarytree_nodes(tree.right.right.right, None, BinaryTreeNode(9))
    assert find_path(tree, 23) == [[5,1,2,7,8],[5,4,3,2,9]]
    assert find_path(tree, 15) == []
    assert find_path(tree, 6) == []


def test_special_not_symmetrical_binary_tree():
    #            5
    #          1   4
    #        2       3
    #      7           2
    #    8               
    tree = BinaryTreeNode(5)
    connect_binarytree_nodes(tree, BinaryTreeNode(1), BinaryTreeNode(4))
    connect_binarytree_nodes(tree.left, BinaryTreeNode(2), None)
    connect_binarytree_nodes(tree.right, None, BinaryTreeNode(3))
    connect_binarytree_nodes(tree.left.left, BinaryTreeNode(7), None)
    connect_binarytree_nodes(tree.right.right, None, BinaryTreeNode(2))
    connect_binarytree_nodes(tree.left.left.left, BinaryTreeNode(8), None)
    assert find_path(tree, 14) == [[5,4,3,2]]
    assert find_path(tree, 9) == []
    assert find_path(tree, 6) == []


def test_special_not_symmetrical_binary_tree_all_nodes_same():
    #            5
    #          1   4
    #        2       3
    #      7           2
    #    8          9
    tree = BinaryTreeNode(5)
    connect_binarytree_nodes(tree, BinaryTreeNode(1), BinaryTreeNode(4))
    connect_binarytree_nodes(tree.left, BinaryTreeNode(2), None)
    connect_binarytree_nodes(tree.right, None, BinaryTreeNode(3))
    connect_binarytree_nodes(tree.left.left, BinaryTreeNode(7), None)
    connect_binarytree_nodes(tree.right.right, None, BinaryTreeNode(2))
    connect_binarytree_nodes(tree.left.left.left, BinaryTreeNode(8), None)
    connect_binarytree_nodes(tree.right.right.right, BinaryTreeNode(9), None)
    assert find_path(tree, 23) == [[5,1,2,7,8],[5,4,3,2,9]]
    assert find_path(tree, 14) == []
    assert find_path(tree, 6) == []
    


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
    assert find_path(tree, 23) == [[5,4,3,2,9]]
    assert find_path(tree, 22) == []
    assert find_path(tree, 9) == []

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
    assert find_path(tree, 23) == [[5,4,3,2,9]]
    assert find_path(tree, 22) == []
    assert find_path(tree, 9) == []



def test_one_node():
    tree = BinaryTreeNode(5)
    assert find_path(tree, 5) == [[5]]
    assert find_path(tree, 6) == []

def test_none():
    tree = None
    assert find_path(tree, 1) == []




