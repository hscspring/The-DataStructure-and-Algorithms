"""
面试题 18（一）：在 O (1) 时间删除链表结点
题目：给定单向链表的头指针和一个结点指针，定义一个函数在 O (1) 时间删除该结点。

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

def delete_node(root: Node, node: Node) -> Node:
    """
    Given a link, delete a node in O(1).

    Parameters
    -----------
    root: Node
        link root
    node: Node
        link node

    Returns
    ---------
    out: Node
        new link

    Notes
    ------
    Copy node.next to node, then delete node.next.
    That's equal to delete node.
    """
    # only one node
    if not root:
        return
    if node == root and not root.next:
        root = None
        node = None
    # node is tail 
    elif not node.next:
        pnode = root
        while pnode.next != node:
            pnode = pnode.next
        pnode.next = None
        node = None
    else:
        pnext = node.next
        node.val = pnext.val
        node.next = pnext.next
        pnext = None
    return root



if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    root = list2link(lst)
    print(link2list(root))




