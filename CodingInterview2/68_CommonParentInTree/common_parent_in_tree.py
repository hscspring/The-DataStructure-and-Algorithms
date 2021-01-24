"""
面试题 68：树中两个结点的最低公共祖先
题目：输入两个树结点，求它们的最低公共祖先。
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.children = []


def connect(parent: Node, children: list) -> Node:
    if parent:
        parent.children = children
    return parent


def get_node_path(tree: Node, node: Node, res: list) -> bool:
    res.append(tree.val)
    found = False
    if tree.val == node.val:
        return True
    for i in range(len(tree.children)):
        if not found:
            found = get_node_path(tree.children[i], node, res)
    if not found:
        res.pop()
    return found


def get_last_common_node(path1: list, path2: list) -> int:
    i = 0
    last = None
    while i < len(path1) and i < len(path2):
        if path1[i] == path2[i]:
            last = path1[i]
        i += 1
    return last


def get_last_common_parent(tree: Node, node1: Node, node2: Node) -> Node:
    """

    Parameters
    -----------

    Returns
    ---------


    Notes
    ------

    """
    if not tree or not node1 or not node1:
        return None

    path1, path2 = [], []
    get_node_path(tree, node1, path1)
    get_node_path(tree, node2, path2)

    pare1, pare2 = path1[:-1], path2[:-1]
    common = get_last_common_node(pare1, pare2)

    return common


if __name__ == '__main__':
    p4 = connect(Node(4), [Node(6), Node(7)])
    p5 = connect(Node(5), [Node(8), Node(9), Node(10)])
    p2 = connect(Node(2), [p4, p5])
    tree = connect(Node(1), [p2, Node(3)])

    # print(tree.val)
    # print(tree.children)
    # print(tree.children[0].val)
    # res = []
    # get_node_path(tree, Node(8), res)
    # print(res)

    res = get_last_common_parent(tree, Node(0), Node(8))
    print(res)
