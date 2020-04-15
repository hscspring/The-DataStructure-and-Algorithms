"""
面试题55（二）：平衡二叉树
题目：输入一棵二叉树的根结点，判断该树是不是平衡二叉树。如果某二叉树中
任意结点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

"""

class BSTNode:
    """docstring for BSTNode"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def connect_bst_nodes(head: BSTNode, left: BSTNode, right: BSTNode) -> BSTNode:
    if head:
        head.left = left
        head.right = right


def tree_depth(bst: BSTNode) -> int:
    if not bst:
        return 0
    left = tree_depth(bst.left)
    right = tree_depth(bst.right)
    if left > right:
        return left + 1
    else:
        return right + 1

    # max(depth(bst.left), depth(bst.right)) + 1

def tree_is_balanced(bst: BSTNode) -> bool:
    """
    

    Parameters
    -----------
    lst: the given bst

    Returns
    ---------
    the depth 

    Notes
    ------
    
    """
    if not bst:
        return True
    left = tree_depth(bst.left)
    right = tree_depth(bst.right)
    diff = left - right
    if diff > 1 or diff < -1:
        return False
    return tree_is_balanced(bst.left) and tree_is_balanced(bst.right)





def dfs_height(bst: BSTNode) -> int:
    if not bst:
        return 0
    left = dfs_height(bst.left)
    if left == -1: return -1
    right = dfs_height(bst.right)
    if right == -1: return -1

    diff = left - right
    if diff > 1 or diff < -1: return -1

    return max(left, right) + 1


def tree_is_balanced2(bst: BSTNode) -> bool:
    return dfs_height(bst) != -1





def tree_is_balanced3(bst: BSTNode) -> bool:
    # or set res as a global variable
    return get_height(bst)[1]

def get_height(bst: BSTNode):
    if not bst:
        return 0, True
    left, res = get_height(bst.left)
    right, res = get_height(bst.right)
    diff = left - right
    if diff > 1 or diff < -1:
        res = False
    return max(left, right) + 1, res





if __name__ == '__main__':
    tree = BSTNode(10)
    connect_bst_nodes(tree, BSTNode(6), BSTNode(14))
    connect_bst_nodes(tree.left, BSTNode(4), BSTNode(8))
    connect_bst_nodes(tree.right, BSTNode(12), BSTNode(16))

    tree = BSTNode(1)
    connect_bst_nodes(tree, None, BSTNode(2))
    connect_bst_nodes(tree.right, None, BSTNode(3))
    connect_bst_nodes(tree.right.right, None, BSTNode(4))
    connect_bst_nodes(tree.right.right.right, None, BSTNode(5))


    tree = BSTNode(1)
    connect_bst_nodes(tree, BSTNode(2), BSTNode(2))
    connect_bst_nodes(tree.left, BSTNode(3), None)
    connect_bst_nodes(tree.right, None, BSTNode(3))
    connect_bst_nodes(tree.left.left, BSTNode(4), None)
    connect_bst_nodes(tree.right.right, None, BSTNode(4))



    
    # res = tree_is_balanced(tree)
    # print(res)

    # res = True
    # res = tree_is_balanced3(tree)
    # print(res)

    height = dfs_height(tree)
    print(height)


    print(tree_is_balanced4(tree))








    