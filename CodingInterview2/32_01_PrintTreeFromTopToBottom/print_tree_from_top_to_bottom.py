"""
面试题32（一）：不分行从上往下打印二叉树
题目：从上往下打印出二叉树的每个结点，同一层的结点按照从左到右的顺序打印。

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
    Print tree from top to bottom.

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
    pass
    




    