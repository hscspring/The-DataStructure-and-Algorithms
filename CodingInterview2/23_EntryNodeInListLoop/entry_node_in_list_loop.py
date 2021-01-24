"""

面试题 23：链表中环的入口结点
题目：一个链表中包含环，如何找出环的入口结点？例如，在图 3.8 的链表中，
环的入口结点是结点 3。
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

def list2link_withloop(lst, entry_index):
    root = Node(None)
    ptr = root
    for i in lst:
        ptr.next = Node(i)
        ptr = ptr.next
    node = root.next
    n = 0
    while node:
        if n == entry_index:
            ptr.next = node
            break
        node = node.next
        n += 1
    return root.next

def link2list(root: Node) -> list:
    res = []
    while root:
        res.append(root.val)
        root = root.next
    return res

def find_entry_node_of_loop(link: Node) -> Node:
    """
    Given a linklist, find the entry node of the loop in the linklist.

    Parameters
    -----------
    link: Node
        the given linklist.
    Returns
    ---------
    out: Node
        the entry of the loop.

    Notes
    ------
    1. make sure there is a loop
    2. calculate the length of the loop
    3. find the entry node
    """
    loop_len = there_is_loop(link)
    if not loop_len:
        return None
    first, second = link, link
    for i in range(loop_len):
        first = first.next
    while first:
        if first.val == second.val:
            break
        first = first.next
        second = second.next
    return first

def there_is_loop(link: Node) -> int:
    """
    Returns 0 if there isn't a loop, else the length of the loop.
    """
    if not link or not link.next:
        return 0
    fast, slow = link, link
    length = 0
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
        if fast.val == slow.val:
            tag = slow.val
            while slow.next:
                length += 1
                slow = slow.next
                if slow.val == tag:
                    return length
    return length



def find_entry_node_of_loop2(link: Node) -> Node:
    has_meet = meet(link)
    if not has_meet:
        return None
    
    length = 0
    node = has_meet
    while node.next != has_meet:
        length += 1
        node = node.next
    
    first = link
    for i in range(length+1):
        first = first.next
    second = link
    while first != second:
        first = first.next
        second = second.next
    return first


def meet(link: Node):
    if not link or not link.next:
        return None
    slow = link.next
    fast = link.next.next
    while slow and fast:
        if slow.val == fast.val:
            return fast
        slow = slow.next
        fast = fast.next
        if fast:
            fast = fast.next
    return None

if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6]
    link = list2link_withloop(lst, 2)
    # link = list2link(lst)
    # print(there_is_loop(link))
    # n = 0
    # while link:
    #     n += 1
    #     print(link.val)
    #     link = link.next
    #     if n > 20:
    #         break
    # res = find_entry_node_of_loop(link)
    # print(res.val)
    res = find_entry_node_of_loop2(link)
    print(res)







