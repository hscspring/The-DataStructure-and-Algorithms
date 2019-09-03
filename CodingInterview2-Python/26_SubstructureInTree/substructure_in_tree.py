"""
面试题 26：树的子结构
题目：输入两棵二叉树 A 和 B，判断 B 是不是 A 的子结构。

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

def has_subtree(bt1: BinaryTreeNode, bt2: BinaryTreeNode) -> bool:
    """
    Given two BinaryTree, whether one tree is the subtree of another.

    Parameters
    -----------
    bt1: BinaryTreeNode
    bt2: BinaryTreeNode

    Returns
    ---------
    out: bool

    Notes
    ------
    - find the parent value that is the same as subtree
    - recursively judge the left and right node
    """
    res = False
    if bt1 and bt2:
        if equal(bt1.val, bt2.val):
            res = is_bt2_subtree_of_bt1(bt1, bt2)
        if not res:
            res = has_subtree(bt1.left, bt2)
        if not res:
            res = has_subtree(bt1.right, bt2)
    return res


def is_bt2_subtree_of_bt1(bt1: BinaryTreeNode, bt2: BinaryTreeNode) -> bool:
    if not bt2:
        return True
    if not bt1:
        return False
    if not equal(bt1.val, bt2.val):
        return False
    return (is_bt2_subtree_of_bt1(bt1.left, bt2.left) and
            is_bt2_subtree_of_bt1(bt1.right, bt2.right))


def equal(num1, num2) -> bool:
    return abs(num1 - num2) < 1e-7


if __name__ == '__main__':
    
    tree = BinaryTreeNode(5)
    connect_binarytree_nodes(tree, BinaryTreeNode(4), None)
    connect_binarytree_nodes(tree.left, BinaryTreeNode(3), None)
    connect_binarytree_nodes(tree.left.left, BinaryTreeNode(2), None)
    connect_binarytree_nodes(tree.left.left.left, BinaryTreeNode(9), None)

    print_tree(tree)

    subtree = BinaryTreeNode(4)
    connect_binarytree_nodes(subtree, BinaryTreeNode(3), None)
    connect_binarytree_nodes(subtree.left, BinaryTreeNode(2), None)

    print_tree(subtree)

    res = has_subtree(tree, subtree)
    print(res)






