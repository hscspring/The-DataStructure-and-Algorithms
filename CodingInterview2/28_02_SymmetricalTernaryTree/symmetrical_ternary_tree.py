"""
面试题 28：对称的三叉树
题目：请实现一个函数，用来判断一棵三叉树是不是对称的。如果一棵三叉树和
它的镜像一样，那么它是对称的。

"""


class TernaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.mid = None
        self.right = None


def connect_ternarytree_nodes(parent: TernaryTreeNode,
                             left: TernaryTreeNode,
                             mid: TernaryTreeNode,
                             right: TernaryTreeNode
                             ) -> TernaryTreeNode:
    if parent:
        parent.left = left
        parent.mid = mid
        parent.right = right
    return parent


def print_node(node: TernaryTreeNode):
    if node:
        print("node value: ", node.val)
        if node.left:
            print("left child value: ", node.left.val)
        else:
            print("left child null")
        if node.right:
            print("right child value: ", node.right.val)
        if node.mid:
            print("mid child value: ", node.mid.val)
        else:
            print("right child null")
    else:
        print("node is null")


def print_tree(root: TernaryTreeNode):
    print_node(root)
    if root:
        if root.left:
            print_tree(root.left)
        if root.right:
            print_tree(root.right)
        if root.mid:
            print_tree(root.mid)


def is_symmetrical(bt: TernaryTreeNode) -> bool:
    """
    Whether the given TernaryTree is symmetrical.

    Parameters
    -----------
    bt: TernaryTreeNode

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


def preorder(bt: TernaryTreeNode, res: list) -> list:
    if not bt:
        res.append(None)
        return res
    res.append(bt.val)
    preorder(bt.left, res)
    preorder(bt.mid, res)
    preorder(bt.right, res)


def symmetrical_preorder(bt: TernaryTreeNode, res: list) -> list:
    if not bt:
        res.append(None)
        return res
    res.append(bt.val)
    symmetrical_preorder(bt.right, res)
    symmetrical_preorder(bt.mid, res)
    symmetrical_preorder(bt.left, res)


def is_symmetrical_recursion(bt: TernaryTreeNode) -> bool:
    return is_symmetrical_recursion_core(bt, bt)


def is_symmetrical_recursion_core(bt1, bt2) -> bool:
    if not bt1 and not bt2:
        return True
    if not bt1 or not bt2:
        return False
    if bt1.val != bt2.val:
        return False
    return (is_symmetrical_recursion_core(bt1.left, bt2.right) and
            is_symmetrical_recursion_core(bt1.right, bt2.left) and
            is_symmetrical_recursion_core(bt1.mid, bt2.mid))


if __name__ == '__main__':

    tree = TernaryTreeNode(1)
    connect_ternarytree_nodes(tree, TernaryTreeNode(2), TernaryTreeNode(3), TernaryTreeNode(2))
    connect_ternarytree_nodes(tree.left, TernaryTreeNode(5), TernaryTreeNode(6), TernaryTreeNode(5))
    connect_ternarytree_nodes(tree.mid, TernaryTreeNode(8), TernaryTreeNode(9), TernaryTreeNode(9))
    connect_ternarytree_nodes(tree.right, TernaryTreeNode(5), TernaryTreeNode(6), TernaryTreeNode(5))


    res = []
    preorder(tree, res)
    print(res)

    ress = []
    symmetrical_preorder(tree, ress)
    print(ress)


    print(is_symmetrical(tree))

    print(is_symmetrical_recursion(tree))




