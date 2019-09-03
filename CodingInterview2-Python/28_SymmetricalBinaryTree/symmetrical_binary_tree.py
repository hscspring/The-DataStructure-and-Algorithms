"""
面试题 28：对称的二叉树
题目：请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和
它的镜像一样，那么它是对称的。

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


def is_symmetrical(bt: BinaryTreeNode) -> bool:
    """
    Whether the given BinaryTree is symmetrical.

    Parameters
    -----------
    bt: BinaryTreeNode

    Returns
    ---------
    out: bool

    Notes
    ------
    Whether the preorder traversal is the same as symmetrical preorder traversal.
    Or is the same as its mirror.
    """
    if not bt:
        return True

    pre, spre = [], []
    preorder(bt, pre)
    symmetrical_preorder(bt, spre)
    return pre == spre


def preorder(bt: BinaryTreeNode, res: list) -> list:
    if not bt:
        res.append(None)
        return res
    res.append(bt.val)
    if not bt.left and not bt.right:
        res.append(None)
        res.append(None)
    preorder(bt.left, res)
    preorder(bt.right, res)


def symmetrical_preorder(bt: BinaryTreeNode, res: list) -> list:
    if not bt:
        res.append(None)
        return res
    res.append(bt.val)
    if not bt.left and not bt.right:
        res.append(None)
        res.append(None)
    symmetrical_preorder(bt.right, res)
    symmetrical_preorder(bt.left, res)


def is_symmetrical_recursion(bt: BinaryTreeNode) -> bool:
    return is_symmetrical_recursion_core(bt, bt)


def is_symmetrical_recursion_core(bt1, bt2) -> bool:
    if not bt1 and not bt2:
        return True
    if not bt1 or not bt2:
        return False
    if bt1.val != bt2.val:
        return False
    return (is_symmetrical_recursion_core(bt1.left, bt2.right) and
            is_symmetrical_recursion_core(bt1.right, bt2.left))


if __name__ == '__main__':
    #    5
    #  5   5
    # 5   5
    tree = BinaryTreeNode(5)
    connect_binarytree_nodes(tree, BinaryTreeNode(5), BinaryTreeNode(5))
    connect_binarytree_nodes(tree.left, BinaryTreeNode(5), None)
    connect_binarytree_nodes(tree.right, BinaryTreeNode(5), None)

    # tree = BinaryTreeNode(7)
    # connect_binarytree_nodes(tree, BinaryTreeNode(7), BinaryTreeNode(7))
    # connect_binarytree_nodes(tree.left, BinaryTreeNode(7), BinaryTreeNode(7))
    # connect_binarytree_nodes(tree.right, BinaryTreeNode(7), None)

    res = []
    preorder(tree, res)
    print(res)

    ress = []
    symmetrical_preorder(tree, ress)
    print(ress)

    print(is_symmetrical(tree))

    print(is_symmetrical_recursion(tree))




