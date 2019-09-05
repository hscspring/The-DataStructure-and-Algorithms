"""
面试题 32（二）：分行从上到下打印二叉树
题目：从上到下按层打印二叉树，同一层的结点按从左到右的顺序打印，每一层
打印到一行。
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


def print_binary_tree(tree: BinaryTreeNode) -> list:
    """
    Print tree from top to bottom by level.

    Parameters
    -----------
    binary_tree: BinaryTreeNode

    Returns
    ---------
    out: list
        Tree items list.

    Notes
    ------

    """
    if not tree:
        return []
    queue = [tree]
    res = []
    while len(queue):
        node = queue.pop(0)
        res.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return res







if __name__ == '__main__':
    tree = BinaryTreeNode(7)
    connect_binarytree_nodes(tree, BinaryTreeNode(4), BinaryTreeNode(7))
    connect_binarytree_nodes(tree.left, BinaryTreeNode(7), BinaryTreeNode(7))
    connect_binarytree_nodes(tree.right, BinaryTreeNode(5), None)
    res = print_binary_tree(tree)
    print(res)
    




    