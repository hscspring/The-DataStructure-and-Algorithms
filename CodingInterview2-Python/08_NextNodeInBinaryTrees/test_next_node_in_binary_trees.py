from next_node_in_binary_trees import TreeNode, get_next_in_inorder, connect_nodes


def test_normal_bt():
    #           8
    #       6      10
    #      5 7    9  11
    tree = TreeNode(8)
    connect_nodes(tree, TreeNode(6), TreeNode(10))
    connect_nodes(tree.left, TreeNode(5), TreeNode(7))
    connect_nodes(tree.right, TreeNode(9), TreeNode(11))
    pnext = get_next_in_inorder(tree)
    assert pnext.val == 9
    pnext = get_next_in_inorder(tree.left)
    assert pnext.val == 7
    pnext = get_next_in_inorder(tree.left.left)
    assert pnext.val == 6


def test_left_bt():
    #            5
    #          4
    #        3
    #      2
    tree = TreeNode(5)
    connect_nodes(tree, TreeNode(4), None)
    connect_nodes(tree.left, TreeNode(3), None)
    connect_nodes(tree.left.left, TreeNode(2), None)
    pnext = get_next_in_inorder(tree.left)
    assert pnext.val == 5

def test_left_special_bt():
    #            5
    #          4
    #        3    1
    #      2
    tree = TreeNode(5)
    connect_nodes(tree, TreeNode(4), None)
    connect_nodes(tree.left, TreeNode(3), TreeNode(1))
    connect_nodes(tree.left.left, TreeNode(2), None)
    pnext = get_next_in_inorder(tree.left.right)
    # 1's next
    assert pnext.val == 5

def test_right_bt():
    #        2
    #         3
    #          4
    #           5
    tree = TreeNode(2)
    connect_nodes(tree, None, TreeNode(3))
    connect_nodes(tree.right, None, TreeNode(4))
    connect_nodes(tree.right.right, None, TreeNode(5))
    pnext = get_next_in_inorder(tree)
    assert pnext.val == 3

def test_none():
    tree = None
    pnext = get_next_in_inorder(tree)
    assert pnext == None


