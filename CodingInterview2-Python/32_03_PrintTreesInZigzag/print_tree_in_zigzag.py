"""
面试题 32（三）：之字形打印二叉树
题目：请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺
序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，
其他行以此类推。
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
    stack1, stack2 = [tree], []
    q1res, q2res = [], []
    res = []
    while True:
        while len(stack1):
            node = stack1.pop()
            q1res.append(node.val)
            if node.left:
                stack2.append(node.left)
            if node.right:
                stack2.append(node.right)
        if q2res:
            res.append(q2res)
            q2res = []
        while len(stack2):
            node = stack2.pop()
            q2res.append(node.val)
            if node.right:
                stack1.append(node.right)
            if node.left:
                stack1.append(node.left)
        if q1res:
            res.append(q1res)
            q1res = []
        if not stack1 and not stack2:
            break
    return res


def print_binary_tree2(tree: BinaryTreeNode) -> list:
    if not tree:
        return []
    stack1, stack2 = [tree], []
    res = []
    while stack1 or stack2:
        tmp = []
        while stack1: # for i in range(len(stack1))
            node = stack1.pop()
            tmp.append(node.val)
            if node.left:
                stack2.append(node.left)
            if node.right:
                stack2.append(node.right)
        if tmp:
            res.append(tmp)
            tmp = []
        while stack2: #for i in range(len(stack2)):
            node = stack2.pop()
            tmp.append(node.val)
            if node.right:
                stack1.append(node.right)
            if node.left:
                stack1.append(node.left)
        if tmp:
            res.append(tmp)
    return res


def print_binary_tree3(tree: BinaryTreeNode) -> list:
    if not tree:
        return []
    queue, res = [tree], []
    depth = 0
    while queue:
        depth += 1
        tmp = []
        for i in range(len(queue)):
            node = queue.pop(0)
            tmp.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if depth % 2 == 0:
            tmp.reverse()
        if tmp:
            res.append(tmp)
    return res

def print_binary_tree4(tree: BinaryTreeNode) -> list:
    if not tree:
        return []
    stacks = [[tree], []]
    cur, nxt = 0, 1
    res, tmp = [], []
    while stacks[0] or stacks[1]:
        node = stacks[cur].pop()
        tmp.append(node.val)
        if cur == 0:
            if node.left:
                stacks[nxt].append(node.left)
            if node.right:
                stacks[nxt].append(node.right)
        else:
            if node.right:
                stacks[nxt].append(node.right)
            if node.left:
                stacks[nxt].append(node.left)
        if not stacks[cur]:
            cur = 1 - cur
            nxt = 1 - nxt
            res.append(tmp)
            tmp = []

    return res

if __name__ == '__main__':
    tree = BinaryTreeNode(8)
    connect_binarytree_nodes(tree, BinaryTreeNode(7), BinaryTreeNode(6))
    connect_binarytree_nodes(tree.left, BinaryTreeNode(5), BinaryTreeNode(3))
    connect_binarytree_nodes(tree.right, BinaryTreeNode(2), None)
    res = print_binary_tree4(tree)
    print(res)
    




    