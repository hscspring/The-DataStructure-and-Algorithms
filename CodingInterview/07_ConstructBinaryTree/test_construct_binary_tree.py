from construct_binary_tree import reconstruct_bianary_tree
from construct_binary_tree import bfs


def test_normal_bt():
    preorder = [1, 2, 4, 7, 3, 5, 6, 8]
    inorder = [4, 7, 2, 1, 5, 3, 8, 6]
    bt = reconstruct_bianary_tree(preorder, inorder)
    assert bfs(bt) == [1, 2, 3, 4, 'null', 5, 6, 'null', 7, 'null', 'null', 8]

def test_left_bt():
    preorder = [1, 2, 3, 4, 5]
    inorder = [5, 4, 3, 2, 1]
    bt = reconstruct_bianary_tree(preorder, inorder)
    assert bfs(bt) == [1, 2, "null", 3, "null", 4, "null", 5]

def test_right_bt():
    preorder = [1, 2, 3, 4, 5]
    inorder = [1, 2, 3, 4, 5]
    bt = reconstruct_bianary_tree(preorder, inorder)
    assert bfs(bt) == [1, "null", 2, "null", 3, "null", 4, "null", 5]

def test_complete_bt():
    preorder = [1, 2, 4, 5, 3, 6, 7]
    inorder = [4, 2, 5, 1, 6, 3, 7]
    bt = reconstruct_bianary_tree(preorder, inorder)
    assert bfs(bt) == [1, 2, 3, 4, 5, 6, 7]

def test_none_bt():
    preorder = []
    inorder = []
    bt = reconstruct_bianary_tree(preorder, inorder)
    assert bfs(bt) == []

def test_not_match_bt():
    preorder = [1, 2, 4, 5, 3, 6, 7]
    inorder = [4, 2, 8, 1, 6, 3, 7]
    bt = reconstruct_bianary_tree(preorder, inorder)
    assert bfs(bt) == []
