"""
面试题 25：合并两个排序的链表
题目：输入两个递增排序的链表，合并这两个链表并使新链表中的结点仍然是按
照递增排序的。例如输入图 3.11 中的链表 1 和链表 2，则合并之后的升序链表如链
表 3 所示。

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def list2link(lst):
    root = Node(None)
    ptr = root
    for i in lst:
        ptr.next = Node(i)
        ptr = ptr.next
    return root.next


def link2list(root: Node) -> list:
    res = []
    while root:
        res.append(root.val)
        root = root.next
    return res


def merge(link1: Node, link2: Node) -> Node:
    """
    Merge two linklists.

    Parameters
    -----------
    link1: Node
    link2: Node

    Returns
    ---------
    out: Node

    Notes
    ------

    """
    link = Node(None)
    ptr = link
    while link1 and link2:
        if link1.val <= link2.val:
            ptr.next = Node(link1.val)
            ptr = ptr.next
            link1 = link1.next
        else:
            ptr.next = Node(link2.val)
            ptr = ptr.next
            link2 = link2.next
    while link1:
        ptr.next = Node(link1.val)
        ptr = ptr.next
        link1 = link1.next
    while link2:
        ptr.next = Node(link2.val)
        ptr = ptr.next
        link2 = link2.next
    return link.next


def merge_recurision(link1: Node, link2: Node) -> Node:
    if not link1:
        return link2
    if not link2:
        return link1
    if link1.val < link2.val:
        link = link1
        link.next = merge_recurision(link1.next, link2)
    else:
        link = link2
        link.next = merge_recurision(link1, link2.next)
    return link


if __name__ == '__main__':
    lst1 = [1, 3, 5]
    lst2 = [2, 4, 6]
    link1 = list2link(lst1)
    link2 = list2link(lst2)
    link = merge(link1, link2)
    print(link2list(link))
    print(link2list(link1))
    print(link2list(link2))
