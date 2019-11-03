# -*- coding: utf-8 -*-

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def connect(parent, left, right):
    if parent:
        parent.left = left
        parent.right = right
    return parent

def get_node_path(tree, node, res):
    res.append(tree.val)
    found = False
    if tree.val == node.val:
        return True
    # for subtree in [tree.left, tree.right]:
    #     if subtree and not found:
    #         found = get_node_path(subtree, node, res)
    if tree.left and not found:
        found = get_node_path(tree.left, node, res)
    if tree.right and not found:
        found = get_node_path(tree.right, node, res)
    if not found:
        res.pop()
    return found

if __name__ == '__main__':
    root = Node(1)
    tree = connect(root, Node(2), Node(3))
    tree.left = connect(tree.left, Node(20), Node(21))

    node = Node(20)
    res = []
    get_node_path(tree, node, res)
    print(res)

    node = Node(21)
    res = []
    get_node_path(tree, node, res)
    print(res)
    print(tree.left.left.val)
