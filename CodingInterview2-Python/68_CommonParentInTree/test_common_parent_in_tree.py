from common_parent_in_tree import get_last_common_parent
from common_parent_in_tree import connect, Node


def test_normal():
    #             1
    #           /   \
    #          2     3
    #       /     \
    #      4       5
    #     / \    / |  \
    #    6   7  8  9  10
    p4 = connect(Node(4), [Node(6), Node(7)])
    p5 = connect(Node(5), [Node(8), Node(9), Node(10)])
    p2 = connect(Node(2), [p4, p5])
    tree = connect(Node(1), [p2, Node(3)])

    assert get_last_common_parent(tree, Node(6), Node(8)) == 2
    assert get_last_common_parent(tree, Node(6), Node(9)) == 2
    assert get_last_common_parent(tree, Node(6), Node(7)) == 4
    assert get_last_common_parent(tree, Node(2), Node(8)) == 1
    assert get_last_common_parent(tree, Node(1), Node(8)) == None
    assert get_last_common_parent(tree, Node(4), Node(5)) == 2
    assert get_last_common_parent(tree, Node(8), Node(9)) == 5
    assert get_last_common_parent(tree, Node(3), Node(10)) == 1


def test_tree_is_link():
    #               1
    #              /
    #             2
    #            /
    #           3
    #          /
    #         4
    #        /
    #       5
    p4 = connect(Node(4), [Node(5)])
    p3 = connect(Node(3), [p4])
    p2 = connect(Node(2), [p3])
    tree = connect(Node(1), [p2])

    assert get_last_common_parent(tree, Node(5), Node(4)) == 3
    assert get_last_common_parent(tree, Node(5), Node(3)) == 2
    assert get_last_common_parent(tree, Node(6), Node(2)) == None


def test_none():
    tree = None
    assert get_last_common_parent(tree, Node(6), Node(2)) == None
