"""
面试题 37：序列化二叉树
题目：请实现两个函数，分别用来序列化和反序列化二叉树。

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

def travel_preorder(bt: BinaryTreeNode, res: list) -> list:
    if not bt:
        res.append("$")
        return res
    res.append(bt.val)
    travel_preorder(bt.left, res)
    travel_preorder(bt.right, res)
    return res

def serialize(bt: BinaryTreeNode, res: list) -> list:
    """
    serialize a binary tree.

    Parameters
    -----------
    bt: the given binary tree

    Returns
    ---------
    out: serialized string of the tree.

    Notes
    ------

    """
    if not bt:
        res.append("$")
        return res
    res.append(bt.val)
    serialize(bt.left, res)
    serialize(bt.right, res)
    return res

def serialize1(bt: BinaryTreeNode, serial: list) -> list:
    if bt:
        serial.append(bt.val)
        serialize1(bt.left, serial)
        serialize1(bt.right, serial)
    else:
        serial.append("$")
    return serial

def deserialize(serial: list) -> BinaryTreeNode:
    if not serial:
        return None

    head = None
    value = serial.pop(0)
    if value != "$":
        head = BinaryTreeNode(value)
        head.left = deserialize(serial)
        head.right = deserialize(serial)
    return head


if __name__ == '__main__':
    tree = BinaryTreeNode(1)
    connect_binarytree_nodes(tree, BinaryTreeNode(2), BinaryTreeNode(3))
    connect_binarytree_nodes(tree.left, BinaryTreeNode(4), None)
    connect_binarytree_nodes(tree.right, BinaryTreeNode(5), BinaryTreeNode(6))
    
    
    # res = travel_preorder(tree, [])
    # print(res)

    serial = serialize(tree, [])
    print(serial)

    head = deserialize(serial)
    res = travel_preorder(head, [])
    print(res)









    