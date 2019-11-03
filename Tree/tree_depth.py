# -*- coding: utf-8 -*-

def depth(tree):
    if not tree:
        return 0
    left = depth(tree.left)
    right = depth(tree.right)
    return max(left, right) + 1


def balanced(tree):
    if not tree:
        return 0
    left = balanced(tree.left)
    right = balanced(tree.right)
    diff = left - right
    if left == -1 or right == -1 or diff > 1 or diff < -1:
        return -1
    return max(left, right) + 1

