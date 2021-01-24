"""

面试题 34：二叉树中和为某一值的路径
题目：输入一棵二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所
有路径。从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
"""


class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def connect_binarytree_nodes(parent: BinaryTreeNode,
                             left: BinaryTreeNode,
                             right: BinaryTreeNode) -> BinaryTreeNode:
    if parent:
        parent.left = left
        parent.right = right
    return parent



def find_path(bt: BinaryTreeNode, psum: int) -> list:
    """
    Find path in the given bt, which summation is equal to psum.

    Parameters
    -----------
    bt: the given binary tree.
    psum: the given number.

    Returns
    ---------
    out: paths which their summation is equal to psum.

    Notes
    ------
    A path is from the root the one of the leaves.
    """
    if not bt:
        return []
    path, paths = [], []
    find_path_core(bt, psum, path, paths, 0)
    return paths


def find_path_core(bt: BinaryTreeNode, psum: int,
                   path: list, paths: list, curr_sum: int) -> list:
    curr_sum += bt.val
    path.append(bt.val)
    if curr_sum == psum and not bt.left and not bt.right:
        paths.append(path.copy())
    if bt.left:
        find_path_core(bt.left, psum, path, paths, curr_sum)
    if bt.right:
        find_path_core(bt.right, psum, path, paths, curr_sum)
    if path:
        curr_sum -= path.pop()



if __name__ == '__main__':
    tree = BinaryTreeNode(5)
    connect_binarytree_nodes(tree, BinaryTreeNode(1), BinaryTreeNode(4))
    connect_binarytree_nodes(tree.left, BinaryTreeNode(2), None)
    connect_binarytree_nodes(tree.right, None, BinaryTreeNode(3))
    connect_binarytree_nodes(tree.left.left, BinaryTreeNode(7), None)
    connect_binarytree_nodes(tree.right.right, None, BinaryTreeNode(2))
    connect_binarytree_nodes(tree.left.left.left, BinaryTreeNode(8), None)
    connect_binarytree_nodes(tree.right.right.right, None, BinaryTreeNode(9))
    res = find_path(tree, 23)
    print(res)





