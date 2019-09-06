from print_tree_in_lines import print_binary_tree, print_binary_tree2, print_binary_tree3
from print_tree_in_lines import BinaryTreeNode, connect_binarytree_nodes


def test_full_binary_tree():
    #        8
    #    6       6
    #   5 7    7   5
    tree = BinaryTreeNode(8)
    connect_binarytree_nodes(tree, BinaryTreeNode(6), BinaryTreeNode(6))
    connect_binarytree_nodes(tree.left, BinaryTreeNode(5), BinaryTreeNode(7))
    connect_binarytree_nodes(tree.right, BinaryTreeNode(7), BinaryTreeNode(5))
    assert print_binary_tree(tree) == [[8],[6,6],[5,7,7,5]]
    assert print_binary_tree2(tree) == [[8],[6,6],[5,7,7,5]]
    assert print_binary_tree3(tree) == [[8],[6,6],[5,7,7,5]]


def test_not_full_binary_tree():
    #        8
    #    6       6
    #   5 7    7
    tree = BinaryTreeNode(8)
    connect_binarytree_nodes(tree, BinaryTreeNode(6), BinaryTreeNode(6))
    connect_binarytree_nodes(tree.left, BinaryTreeNode(5), BinaryTreeNode(7))
    connect_binarytree_nodes(tree.right, BinaryTreeNode(7), None)
    assert print_binary_tree(tree) == [[8],[6,6],[5,7,7]]
    assert print_binary_tree2(tree) == [[8],[6,6],[5,7,7]]
    assert print_binary_tree3(tree) == [[8],[6,6],[5,7,7]]


def test_not_full_binary_tree_simple():
    #        1
    #    3      
    #       2    
    tree = BinaryTreeNode(1)
    connect_binarytree_nodes(tree, BinaryTreeNode(3), None)
    connect_binarytree_nodes(tree.left, None, BinaryTreeNode(2))
    assert print_binary_tree(tree) == [[1],[3],[2]]
    assert print_binary_tree2(tree) == [[1],[3],[2]]
    assert print_binary_tree3(tree) == [[1],[3],[2]]


def test_special_binary_tree():
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
    assert print_binary_tree(tree) == [[5],[4,4],[3,3],[2,2],[9,9]]
    assert print_binary_tree2(tree) == [[5],[4,4],[3,3],[2,2],[9,9]]
    assert print_binary_tree3(tree) == [[5],[4,4],[3,3],[2,2],[9,9]]


def test_special_not_symmetrical_binary_tree():
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
    assert print_binary_tree(tree) == [[5],[4,4],[3,3],[2,2],[9]]
    assert print_binary_tree2(tree) == [[5],[4,4],[3,3],[2,2],[9]]
    assert print_binary_tree3(tree) == [[5],[4,4],[3,3],[2,2],[9]]


def test_special_not_symmetrical_binary_tree_all_nodes_same():
    #            5
    #          5   5
    #        5       5
    #      5           6
    #    4           3
    tree = BinaryTreeNode(5)
    connect_binarytree_nodes(tree, BinaryTreeNode(5), BinaryTreeNode(5))
    connect_binarytree_nodes(tree.left, BinaryTreeNode(5), None)
    connect_binarytree_nodes(tree.right, None, BinaryTreeNode(5))
    connect_binarytree_nodes(tree.left.left, BinaryTreeNode(5), None)
    connect_binarytree_nodes(tree.right.right, None, BinaryTreeNode(6))
    connect_binarytree_nodes(tree.left.left.left, BinaryTreeNode(4), None)
    connect_binarytree_nodes(tree.right.right.right, BinaryTreeNode(3), None)
    assert print_binary_tree(tree) == [[5],[5,5],[5,5],[5,6],[4,3]]
    assert print_binary_tree2(tree) == [[5],[5,5],[5,5],[5,6],[4,3]]
    assert print_binary_tree3(tree) == [[5],[5,5],[5,5],[5,6],[4,3]]


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
    assert print_binary_tree(tree) == [[5],[4],[3],[2],[9]]
    assert print_binary_tree2(tree) == [[5],[4],[3],[2],[9]]
    assert print_binary_tree3(tree) == [[5],[4],[3],[2],[9]]

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
    assert print_binary_tree(tree) == [[5],[4],[3],[2],[9]]
    assert print_binary_tree2(tree) == [[5],[4],[3],[2],[9]]
    assert print_binary_tree3(tree) == [[5],[4],[3],[2],[9]]



def test_one_node():
    tree = BinaryTreeNode(5)
    assert print_binary_tree(tree) == [[5]]
    assert print_binary_tree2(tree) == [[5]]
    assert print_binary_tree3(tree) == [[5]]


def test_none():
    tree = None
    assert print_binary_tree(tree) == []
    assert print_binary_tree2(tree) == []
    assert print_binary_tree3(tree) == []




