"""
面试题 24：反转链表
题目：定义一个函数，输入一个链表的头结点，反转该链表并输出反转后链表的
头结点。

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



def reverse(link: Node) -> Node:
    """
    Reverse a linklist

    Parameters
    -----------
    link: Node
        the given linklist
    Returns
    ---------
    out: Node
        the revsersed linklist

    Notes
    ------

    """
    if not link:
        return None
    pre = None
    while link:
        val = link.val
        node = Node(val)
        node.next = pre
        pre = node
        link = link.next
    return node

def reverse2(link: Node) -> Node:
    pre = None
    cur = link
    while cur:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    return pre


def reverse3(head: Node) -> Node:
    if not head or not head.next:
        return head
    p = reverse3(head.next)
    head.next.next = head
    head.next = None
    return p


if __name__ == '__main__':
    link = list2link([1, 2])
    rlink = reverse3(link)
    print(rlink.val)
    print(rlink.next)
    # res = link2list(rlink)
    # print(res)



