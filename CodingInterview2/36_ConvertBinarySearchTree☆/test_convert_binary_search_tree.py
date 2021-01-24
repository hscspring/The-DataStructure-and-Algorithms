from convert_binary_search_tree import convert_bst_to_sorted_doubly_linked_list
from convert_binary_search_tree import convert_bst_to_sorted_doubly_linked_list_with_inorder
from convert_binary_search_tree import BSTNode, travel_linked_list, connect_bst_nodes


def test_full_binary_tree1():
    #        10
    #    6       14
    #   4 8    12   16
    tree = BSTNode(10)
    connect_bst_nodes(tree, BSTNode(6), BSTNode(14))
    connect_bst_nodes(tree.left, BSTNode(4), BSTNode(8))
    connect_bst_nodes(tree.right, BSTNode(12), BSTNode(16))
    head = convert_bst_to_sorted_doubly_linked_list(tree)
    assert travel_linked_list(head) == [None, 4, 6, 4, 6, 8, 6, 8, 10, 8, 10, 12, 10, 12, 14, 12, 14, 16, 14, 16, None]

def test_full_binary_tree2():    
    tree = BSTNode(10)
    connect_bst_nodes(tree, BSTNode(6), BSTNode(14))
    connect_bst_nodes(tree.left, BSTNode(4), BSTNode(8))
    connect_bst_nodes(tree.right, BSTNode(12), BSTNode(16))
    head = convert_bst_to_sorted_doubly_linked_list_with_inorder(tree)
    assert travel_linked_list(head) == [None, 4, 6, 4, 6, 8, 6, 8, 10, 8, 10, 12, 10, 12, 14, 12, 14, 16, 14, 16, None]


def test_not_full_binary_tree1():
    #        8
    #    6       12
    #   2 7    10
    tree = BSTNode(8)
    connect_bst_nodes(tree, BSTNode(6), BSTNode(12))
    connect_bst_nodes(tree.left, BSTNode(2), BSTNode(7))
    connect_bst_nodes(tree.right, BSTNode(10), None)
    head = convert_bst_to_sorted_doubly_linked_list(tree)
    assert travel_linked_list(head) == [None, 2, 6, 2, 6, 7, 6, 7, 8, 7, 8, 10, 8, 10, 12, 10, 12, None]


def test_not_full_binary_tree2():    
    tree = BSTNode(8)
    connect_bst_nodes(tree, BSTNode(6), BSTNode(12))
    connect_bst_nodes(tree.left, BSTNode(2), BSTNode(7))
    connect_bst_nodes(tree.right, BSTNode(10), None)
    head = convert_bst_to_sorted_doubly_linked_list_with_inorder(tree)
    assert travel_linked_list(head) == [None, 2, 6, 2, 6, 7, 6, 7, 8, 7, 8, 10, 8, 10, 12, 10, 12, None]



def test_left_binary_tree1():
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
    head = convert_bst_to_sorted_doubly_linked_list(tree)
    assert travel_linked_list(head) == [None, 1, 2, 1,2,3,2,3,4,3,4,5,4,5, None]

def test_left_binary_tree2():
    tree = BSTNode(5)
    connect_bst_nodes(tree, BSTNode(4), None)
    connect_bst_nodes(tree.left, BSTNode(3), None)
    connect_bst_nodes(tree.left.left, BSTNode(2), None)
    connect_bst_nodes(tree.left.left.left, BSTNode(1), None)
    head = convert_bst_to_sorted_doubly_linked_list_with_inorder(tree)
    assert travel_linked_list(head) == [None, 1, 2, 1,2,3,2,3,4,3,4,5,4,5, None]



def test_right_binary_tree1():
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
    head = convert_bst_to_sorted_doubly_linked_list(tree)
    assert travel_linked_list(head) == [None, 1, 2, 1,2,3,2,3,4,3,4,5,4,5, None]


def test_right_binary_tree2():    
    tree = BSTNode(1)
    connect_bst_nodes(tree, None, BSTNode(2))
    connect_bst_nodes(tree.right, None, BSTNode(3))
    connect_bst_nodes(tree.right.right, None, BSTNode(4))
    connect_bst_nodes(tree.right.right.right, None, BSTNode(5))
    head = convert_bst_to_sorted_doubly_linked_list_with_inorder(tree)
    assert travel_linked_list(head) == [None, 1, 2, 1,2,3,2,3,4,3,4,5,4,5, None]


def test_one_node1():
    tree = BSTNode(5)
    head = convert_bst_to_sorted_doubly_linked_list(tree)
    assert travel_linked_list(head) == [None, 5, None]


def test_one_node2():    
    tree = BSTNode(5)
    head = convert_bst_to_sorted_doubly_linked_list_with_inorder(tree)
    res = travel_linked_list(head)
    assert res == [None, 5, None]


def test_none():
    tree = None
    head = convert_bst_to_sorted_doubly_linked_list(tree)
    assert travel_linked_list(head) == []
    head = convert_bst_to_sorted_doubly_linked_list_with_inorder(tree)
    assert travel_linked_list(head) == []




