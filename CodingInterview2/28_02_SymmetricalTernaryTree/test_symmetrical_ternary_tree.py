from symmetrical_ternary_tree import is_symmetrical_recursion, is_symmetrical
from symmetrical_ternary_tree import TernaryTreeNode, connect_ternarytree_nodes


def test_full_ternary_tree_is():
    #           1
    #   2       3       2
    # 5 6 5   8 9 8   5 6 5
    tree = TernaryTreeNode(1)
    connect_ternarytree_nodes(tree, TernaryTreeNode(2), TernaryTreeNode(3), TernaryTreeNode(2))
    connect_ternarytree_nodes(tree.left, TernaryTreeNode(5), TernaryTreeNode(6), TernaryTreeNode(5))
    connect_ternarytree_nodes(tree.mid, TernaryTreeNode(8), TernaryTreeNode(9), TernaryTreeNode(8))
    connect_ternarytree_nodes(tree.right, TernaryTreeNode(5), TernaryTreeNode(6), TernaryTreeNode(5))

    assert is_symmetrical_recursion(tree) == True
    assert is_symmetrical(tree) == True


def test_full_ternary_tree_isnot1():
    #           1
    #   2       3       2
    # 5 6 5   8 9 9   5 6 5
    tree = TernaryTreeNode(1)
    connect_ternarytree_nodes(tree, TernaryTreeNode(2), TernaryTreeNode(3), TernaryTreeNode(2))
    connect_ternarytree_nodes(tree.left, TernaryTreeNode(5), TernaryTreeNode(6), TernaryTreeNode(5))
    connect_ternarytree_nodes(tree.mid, TernaryTreeNode(8), TernaryTreeNode(9), TernaryTreeNode(9))
    connect_ternarytree_nodes(tree.right, TernaryTreeNode(5), TernaryTreeNode(6), TernaryTreeNode(5))

    assert is_symmetrical_recursion(tree) == False
    assert is_symmetrical(tree) == False


def test_full_ternary_tree_isnot2():
    #           1
    #   2       3       2
    # 5 6 5   8 9 8   5 6 6
    tree = TernaryTreeNode(1)
    connect_ternarytree_nodes(tree, TernaryTreeNode(2), TernaryTreeNode(3), TernaryTreeNode(2))
    connect_ternarytree_nodes(tree.left, TernaryTreeNode(5), TernaryTreeNode(6), TernaryTreeNode(5))
    connect_ternarytree_nodes(tree.mid, TernaryTreeNode(8), TernaryTreeNode(9), TernaryTreeNode(8))
    connect_ternarytree_nodes(tree.right, TernaryTreeNode(5), TernaryTreeNode(6), TernaryTreeNode(6))

    assert is_symmetrical_recursion(tree) == False
    assert is_symmetrical(tree) == False


def test_full_ternary_tree_isnot3():
    #           1
    #   2       3       2
    # 6 6 5   8 9 8   5 6 5
    tree = TernaryTreeNode(1)
    connect_ternarytree_nodes(tree, TernaryTreeNode(2), TernaryTreeNode(3), TernaryTreeNode(2))
    connect_ternarytree_nodes(tree.left, TernaryTreeNode(6), TernaryTreeNode(6), TernaryTreeNode(5))
    connect_ternarytree_nodes(tree.mid, TernaryTreeNode(8), TernaryTreeNode(9), TernaryTreeNode(8))
    connect_ternarytree_nodes(tree.right, TernaryTreeNode(5), TernaryTreeNode(6), TernaryTreeNode(5))

    assert is_symmetrical_recursion(tree) == False
    assert is_symmetrical(tree) == False



def test_not_full_ternary_tree_is1():
    #           1
    #   2       3       2
    # 5   5   8 9 8   5    5
    tree = TernaryTreeNode(1)
    connect_ternarytree_nodes(tree, TernaryTreeNode(2), TernaryTreeNode(3), TernaryTreeNode(2))
    connect_ternarytree_nodes(tree.left, TernaryTreeNode(5), None, TernaryTreeNode(5))
    connect_ternarytree_nodes(tree.mid, TernaryTreeNode(8), TernaryTreeNode(9), TernaryTreeNode(8))
    connect_ternarytree_nodes(tree.right, TernaryTreeNode(5), None, TernaryTreeNode(5))

    assert is_symmetrical_recursion(tree) == True
    assert is_symmetrical(tree) == True


def test_not_full_ternary_tree_is2():
    #           1
    #   2       3       2
    # 5 6 5   8   8   5 6  5
    tree = TernaryTreeNode(1)
    connect_ternarytree_nodes(tree, TernaryTreeNode(2), TernaryTreeNode(3), TernaryTreeNode(2))
    connect_ternarytree_nodes(tree.left, TernaryTreeNode(5), TernaryTreeNode(6), TernaryTreeNode(5))
    connect_ternarytree_nodes(tree.mid, TernaryTreeNode(8), None, TernaryTreeNode(8))
    connect_ternarytree_nodes(tree.right, TernaryTreeNode(5), TernaryTreeNode(6), TernaryTreeNode(5))

    assert is_symmetrical_recursion(tree) == True
    assert is_symmetrical(tree) == True



def test_not_full_ternary_tree_is3():
    #           1
    #   2       3       2
    # 5   5   8   8   5    5
    tree = TernaryTreeNode(1)
    connect_ternarytree_nodes(tree, TernaryTreeNode(2), TernaryTreeNode(3), TernaryTreeNode(2))
    connect_ternarytree_nodes(tree.left, TernaryTreeNode(5), None, TernaryTreeNode(5))
    connect_ternarytree_nodes(tree.mid, TernaryTreeNode(8), None, TernaryTreeNode(8))
    connect_ternarytree_nodes(tree.right, TernaryTreeNode(5), None, TernaryTreeNode(5))

    assert is_symmetrical_recursion(tree) == True
    assert is_symmetrical(tree) == True

def test_not_full_ternary_tree_is4():
    #           1
    #   2               2
    # 5   5           5    5
    tree = TernaryTreeNode(1)
    connect_ternarytree_nodes(tree, TernaryTreeNode(2), None, TernaryTreeNode(2))
    connect_ternarytree_nodes(tree.left, TernaryTreeNode(5), None, TernaryTreeNode(5))
    connect_ternarytree_nodes(tree.right, TernaryTreeNode(5), None, TernaryTreeNode(5))

    assert is_symmetrical_recursion(tree) == True
    assert is_symmetrical(tree) == True




def test_not_full_ternary_tree_isnot1():
    #           1
    #   2       3       2
    # 5 6 5   8 9 8   5 6 
    tree = TernaryTreeNode(1)
    connect_ternarytree_nodes(tree, TernaryTreeNode(2), TernaryTreeNode(3), TernaryTreeNode(2))
    connect_ternarytree_nodes(tree.left, TernaryTreeNode(5), TernaryTreeNode(6), TernaryTreeNode(5))
    connect_ternarytree_nodes(tree.mid, TernaryTreeNode(8), TernaryTreeNode(9), TernaryTreeNode(8))
    connect_ternarytree_nodes(tree.right, TernaryTreeNode(5), TernaryTreeNode(6), None)

    assert is_symmetrical_recursion(tree) == False
    assert is_symmetrical(tree) == False




def test_not_full_ternary_tree_isnot2():
    #           1
    #   2       3       2
    # 5 6    8 9 8   5 6 5
    tree = TernaryTreeNode(1)
    connect_ternarytree_nodes(tree, TernaryTreeNode(2), TernaryTreeNode(3), TernaryTreeNode(2))
    connect_ternarytree_nodes(tree.left, TernaryTreeNode(5), TernaryTreeNode(6), None)
    connect_ternarytree_nodes(tree.mid, TernaryTreeNode(8), TernaryTreeNode(9), TernaryTreeNode(8))
    connect_ternarytree_nodes(tree.right, TernaryTreeNode(5), TernaryTreeNode(6), TernaryTreeNode(5))

    assert is_symmetrical_recursion(tree) == False
    assert is_symmetrical(tree) == False

def test_not_full_ternary_tree_isnot3():
    #           1
    #   2       3       2
    # 5 6  5  8 8   5 6 5
    tree = TernaryTreeNode(1)
    connect_ternarytree_nodes(tree, TernaryTreeNode(2), TernaryTreeNode(3), TernaryTreeNode(2))
    connect_ternarytree_nodes(tree.left, TernaryTreeNode(5), TernaryTreeNode(6), TernaryTreeNode(5))
    connect_ternarytree_nodes(tree.mid, TernaryTreeNode(8), TernaryTreeNode(8), None)
    connect_ternarytree_nodes(tree.right, TernaryTreeNode(5), TernaryTreeNode(6), TernaryTreeNode(5))

    assert is_symmetrical_recursion(tree) == False
    assert is_symmetrical(tree) == False



def test_not_full_ternary_tree_isnot4():
    #           1
    #   2               2
    # 5   5           5    
    tree = TernaryTreeNode(1)
    connect_ternarytree_nodes(tree, TernaryTreeNode(2), None, TernaryTreeNode(2))
    connect_ternarytree_nodes(tree.left, TernaryTreeNode(5), None, TernaryTreeNode(5))
    connect_ternarytree_nodes(tree.right, TernaryTreeNode(5), None, None)

    assert is_symmetrical_recursion(tree) == False
    assert is_symmetrical(tree) == False

def test_not_full_ternary_tree_isnot5():
    #           1
    #   2               2
    # 5   5           5    6
    tree = TernaryTreeNode(1)
    connect_ternarytree_nodes(tree, TernaryTreeNode(2), None, TernaryTreeNode(2))
    connect_ternarytree_nodes(tree.left, TernaryTreeNode(5), None, TernaryTreeNode(5))
    connect_ternarytree_nodes(tree.right, TernaryTreeNode(5), None, TernaryTreeNode(6))

    assert is_symmetrical_recursion(tree) == False
    assert is_symmetrical(tree) == False



def test_not_full_ternary_tree_all_nodes_same_isnot1():
    #           1
    #   1       1       1
    # 1 1    1 1 1   1 1 1
    tree = TernaryTreeNode(1)
    connect_ternarytree_nodes(tree, TernaryTreeNode(1), TernaryTreeNode(1), TernaryTreeNode(1))
    connect_ternarytree_nodes(tree.left, TernaryTreeNode(1), TernaryTreeNode(1), None)
    connect_ternarytree_nodes(tree.mid, TernaryTreeNode(1), TernaryTreeNode(1), TernaryTreeNode(1))
    connect_ternarytree_nodes(tree.right, TernaryTreeNode(1), TernaryTreeNode(1), TernaryTreeNode(1))

    assert is_symmetrical_recursion(tree) == False
    assert is_symmetrical(tree) == False


def test_not_full_ternary_tree_all_nodes_same_isnot2():
    #           1
    #   1       1       1
    # 1 1 1   1 1 1   1 1 
    tree = TernaryTreeNode(1)
    connect_ternarytree_nodes(tree, TernaryTreeNode(1), TernaryTreeNode(1), TernaryTreeNode(1))
    connect_ternarytree_nodes(tree.left, TernaryTreeNode(1), TernaryTreeNode(1), TernaryTreeNode(1))
    connect_ternarytree_nodes(tree.mid, TernaryTreeNode(1), TernaryTreeNode(1), TernaryTreeNode(1))
    connect_ternarytree_nodes(tree.right, TernaryTreeNode(1), TernaryTreeNode(1), None)

    assert is_symmetrical_recursion(tree) == False
    assert is_symmetrical(tree) == False


def test_not_full_ternary_tree_all_nodes_same_isnot3():
    #           1
    #   1       1       1
    # 1 1 1   1  1   1 1  1
    tree = TernaryTreeNode(1)
    connect_ternarytree_nodes(tree, TernaryTreeNode(1), TernaryTreeNode(1), TernaryTreeNode(1))
    connect_ternarytree_nodes(tree.left, TernaryTreeNode(1), TernaryTreeNode(1), TernaryTreeNode(1))
    connect_ternarytree_nodes(tree.mid, TernaryTreeNode(1), TernaryTreeNode(1), None)
    connect_ternarytree_nodes(tree.right, TernaryTreeNode(1), TernaryTreeNode(1), TernaryTreeNode(1))

    assert is_symmetrical_recursion(tree) == False
    assert is_symmetrical(tree) == False




def test_one_node():
    tree = TernaryTreeNode(5)
    assert is_symmetrical_recursion(tree) == True
    assert is_symmetrical(tree) == True


def test_none():
    tree = None
    assert is_symmetrical_recursion(tree) == True
    assert is_symmetrical(tree) == True






