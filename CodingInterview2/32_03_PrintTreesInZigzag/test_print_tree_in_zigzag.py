from print_tree_in_zigzag import print_binary_tree, print_binary_tree2, print_binary_tree3, print_binary_tree4
from print_tree_in_zigzag import BinaryTreeNode, connect_binarytree_nodes


def test_full_binary_tree():
    #        8
    #    1       2
    #   3 4    7   5
    tree = BinaryTreeNode(8)
    connect_binarytree_nodes(tree, BinaryTreeNode(1), BinaryTreeNode(2))
    connect_binarytree_nodes(tree.left, BinaryTreeNode(3), BinaryTreeNode(4))
    connect_binarytree_nodes(tree.right, BinaryTreeNode(7), BinaryTreeNode(5))
    assert print_binary_tree(tree) == [[8],[2,1],[3,4,7,5]]
    assert print_binary_tree2(tree) == [[8],[2,1],[3,4,7,5]]
    assert print_binary_tree3(tree) == [[8],[2,1],[3,4,7,5]]
    assert print_binary_tree4(tree) == [[8],[2,1],[3,4,7,5]]


def test_not_full_binary_tree():
    #        8
    #    1       2
    #   5 3    7
    tree = BinaryTreeNode(8)
    connect_binarytree_nodes(tree, BinaryTreeNode(1), BinaryTreeNode(2))
    connect_binarytree_nodes(tree.left, BinaryTreeNode(5), BinaryTreeNode(3))
    connect_binarytree_nodes(tree.right, BinaryTreeNode(7), None)
    assert print_binary_tree(tree) == [[8],[2,1],[5,3,7]]
    assert print_binary_tree2(tree) == [[8],[2,1],[5,3,7]]
    assert print_binary_tree3(tree) == [[8],[2,1],[5,3,7]]
    assert print_binary_tree4(tree) == [[8],[2,1],[5,3,7]]


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
    assert print_binary_tree4(tree) == [[1],[3],[2]]


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
    assert print_binary_tree(tree) == [[5],[4,1],[2,3],[2,7],[8,9]]
    assert print_binary_tree2(tree) == [[5],[4,1],[2,3],[2,7],[8,9]]
    assert print_binary_tree3(tree) == [[5],[4,1],[2,3],[2,7],[8,9]]
    assert print_binary_tree4(tree) == [[5],[4,1],[2,3],[2,7],[8,9]]


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
    assert print_binary_tree(tree) == [[5],[4,1],[2,3],[2,7],[8]]
    assert print_binary_tree2(tree) == [[5],[4,1],[2,3],[2,7],[8]]
    assert print_binary_tree3(tree) == [[5],[4,1],[2,3],[2,7],[8]]
    assert print_binary_tree4(tree) == [[5],[4,1],[2,3],[2,7],[8]]


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
    assert print_binary_tree(tree) == [[5],[4,1],[2,3],[2,7],[8,9]]
    assert print_binary_tree2(tree) == [[5],[4,1],[2,3],[2,7],[8,9]]
    assert print_binary_tree3(tree) == [[5],[4,1],[2,3],[2,7],[8,9]]
    assert print_binary_tree4(tree) == [[5],[4,1],[2,3],[2,7],[8,9]]
    


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
    assert print_binary_tree4(tree) == [[5],[4],[3],[2],[9]]

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
    assert print_binary_tree4(tree) == [[5],[4],[3],[2],[9]]



def test_one_node():
    tree = BinaryTreeNode(5)
    assert print_binary_tree(tree) == [[5]]
    assert print_binary_tree2(tree) == [[5]]
    assert print_binary_tree3(tree) == [[5]]
    assert print_binary_tree4(tree) == [[5]]


def test_none():
    tree = None
    assert print_binary_tree(tree) == []
    assert print_binary_tree2(tree) == []
    assert print_binary_tree3(tree) == []
    assert print_binary_tree4(tree) == []




