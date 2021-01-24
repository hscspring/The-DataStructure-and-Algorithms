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
    queue1, queue2 = [tree], []
    q1res, q2res = [], []
    res = []
    while True:
        while len(queue1):
            node = queue1.pop(0)
            q1res.append(node.val)
            if node.left:
                queue2.append(node.left)
            if node.right:
                queue2.append(node.right)
        if q2res:
            res.append(q2res)
            q2res = []
        while len(queue2):
            node = queue2.pop(0)
            q2res.append(node.val)
            if node.left:
                queue1.append(node.left)
            if node.right:
                queue1.append(node.right)
        if q1res:
            res.append(q1res)
            q1res = []
        if not queue1 and not queue2:
            break
    return res


def print_binary_tree2(tree: BinaryTreeNode) -> list:
    if not tree:
        return []
    queue1, queue2 = [tree], []
    res = []
    while queue1 or queue2:
        tmp = []
        while queue1: # for i in range(len(queue1))
            node = queue1.pop(0)
            tmp.append(node.val)
            if node.left:
                queue2.append(node.left)
            if node.right:
                queue2.append(node.right)
        if tmp:
            res.append(tmp)
            tmp = []
        while queue2: #for i in range(len(queue2)):
            node = queue2.pop(0)
            tmp.append(node.val)
            if node.left:
                queue1.append(node.left)
            if node.right:
                queue1.append(node.right)
        if tmp:
            res.append(tmp)
    return res


def print_binary_tree3(tree: BinaryTreeNode) -> list:
    if not tree:
        return []
    queue, res = [tree], []
    while queue:
        tmp = []
        for i in range(len(queue)):
            node = queue.pop(0)
            tmp.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if tmp:
            res.append(tmp)
    return res

def print_binary_tree4(tree: BinaryTreeNode) -> list:
    if not tree:
        return []
    queue, res, tmp = [tree], [], []
    next_level, tobe_print = 0, 1
    while queue:
        node = queue.pop(0)
        tmp.append(node.val)
        if node.left:
            queue.append(node.left)
            next_level += 1
        if node.right:
            queue.append(node.right)
            next_level += 1
        tobe_print -= 1
        if tobe_print == 0:
            tobe_print = next_level
            next_level = 0
            res.append(tmp)
            tmp = []
    return res

if __name__ == '__main__':
    tree = BinaryTreeNode(8)
    connect_binarytree_nodes(tree, BinaryTreeNode(6), BinaryTreeNode(6))
    connect_binarytree_nodes(tree.left, BinaryTreeNode(5), BinaryTreeNode(7))
    connect_binarytree_nodes(tree.right, BinaryTreeNode(7), None)
    res = print_binary_tree4(tree)
    print(res)
    




    