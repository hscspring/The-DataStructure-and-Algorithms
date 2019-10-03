"""
面试题 55（一）：二叉树的深度
题目：输入一棵二叉树的根结点，求该树的深度。从根结点到叶结点依次经过的
结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

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
        return 0
    left = tree_depth(bst.left)
    right = tree_depth(bst.right)
    if left > right:
        return left + 1
    else:
        return right + 1


if __name__ == '__main__':
    tree = BSTNode(10)
    connect_bst_nodes(tree, BSTNode(6), BSTNode(14))
    connect_bst_nodes(tree.left, BSTNode(4), BSTNode(8))
    connect_bst_nodes(tree.right, BSTNode(12), BSTNode(16))
    
    res = tree_depth(tree)
    print(res)











    