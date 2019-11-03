"""
面试题 22：链表中倒数第 k 个结点
题目：输入一个链表，输出该链表中倒数第 k 个结点。为了符合大多数人的习惯，
本题从 1 开始计数，即链表的尾结点是倒数第 1 个结点。例如一个链表有 6 个结点，
从头结点开始它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个结点是
值为 4 的结点。

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

def find_kth_from_tail(link: Node, k: int) -> Node:
    """
    Find the kth node from tail.

    Parameters
    -----------
    link: Node
        given linklist.
    Returns
    ---------
    out: Node
        the kth node from tail.

    Notes
    ------
    Use two pointers
    """
    if k <= 0 or not link:
        return Node(None)

    pnode = link
    pneed = link
    for i in range(k-1):
        if pnode.next:
            pnode = pnode.next
        else:
            return Node(None)
    while pnode.next:
        pnode = pnode.next
        pneed = pneed.next
    return pneed




if __name__ == '__main__':
    link = list2link([1,2,3,4,5])
    lst = link2list(link)
    print(lst)
    res = find_kth_from_tail(link, 5)
    print(res.val)




