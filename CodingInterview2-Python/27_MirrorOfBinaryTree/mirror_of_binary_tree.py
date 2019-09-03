"""
面试题 27：二叉树的镜像
题目：请完成一个函数，输入一个二叉树，该函数输出它的镜像。

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


def print_node(node: BinaryTreeNode):
    if node:
        print("node value: ", node.val)
        if node.left:
            print("left child value: ", node.left.val)
        else:
            print("left child null")
        if node.right:
            print("right child value: ", node.right.val)
        else:
            print("right child null")
    else:
        print("node is null")


def print_tree(root: BinaryTreeNode):
    print_node(root)
    if root:
        if root.left:
            print_tree(root.left)
        if root.right:
            print_tree(root.right)

def mirror_recursion(bt: BinaryTreeNode) -> BinaryTreeNode:
    """
    Mirror of the given BinaryTree.

    Parameters
    -----------
    bt: BinaryTreeNode
        A Binary Tree.
    Returns
    ---------
    out: BinaryTreeNode
        The mirror of the given Binary Tree.

    Notes
    ------

    """
    if not bt:
        return None
    bt.left, bt.right = bt.right, bt.left
    if bt.left:
        mirror_recursion(bt.left)
    if bt.right:
        mirror_recursion(bt.right)
    return bt


def mirror(bt: BinaryTreeNode) -> BinaryTreeNode:
    """
    The most important thing is REVERSE left and right for each node.
    The order is not important.
    """
    if not bt:
        return None
    stack = [bt]
    while stack:
        node = stack.pop() # or stack.pop(0), it's not important
        node.left, node.right = node.right, node.left
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return bt


if __name__ == '__main__':
    tree = BinaryTreeNode(8)
    connect_binarytree_nodes(tree, BinaryTreeNode(6), BinaryTreeNode(10))
    connect_binarytree_nodes(tree.left, BinaryTreeNode(5), BinaryTreeNode(7))
    connect_binarytree_nodes(tree.right, BinaryTreeNode(9), BinaryTreeNode(11))

    print_tree(tree)

    print("="*50)
    mtree = mirror(tree)
    print_tree(mtree)











    