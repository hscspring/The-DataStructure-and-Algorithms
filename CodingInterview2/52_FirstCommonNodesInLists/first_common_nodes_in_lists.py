"""

面试题 52：两个链表的第一个公共结点
题目：输入两个链表，找出它们的第一个公共结点。
"""

def lst2link(lst):
    root = Node(None)
    ptr = root
    for i in lst:
        ptr.next = Node(i)
        ptr = ptr.next
    ptr = root.next
    return ptr

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def find_first_common_node(link1: Node, link2: Node) -> Node:
    """
    

    Parameters
    -----------

    Returns
    ---------


    Notes
    ------
    Those nodes which after the common node are all the same.
    """
    len1 = get_lenth_of_link(link1)
    len2 = get_lenth_of_link(link2)
    if len1 > len2:
        lng = link1
        sht = link2
    else:
        lng = link2
        sht = link1
    for i in range(abs(len1-len2)):
        lng = lng.next
    while lng and sht and lng.val != sht.val:
        lng = lng.next
        sht = sht.next
    cnode = lng
    return cnode


def get_lenth_of_link(link: Node) -> int:
    head = link
    n = 0
    while head:
        n += 1
        head = head.next
    return n





if __name__ == '__main__':
    lst = [1,2,3,4,5]
    link = lst2link(lst)
    lenth = get_lenth_of_link(link)

    link1 = lst2link([1,2,3,4,7])
    link2 = lst2link([5,6,8])
    res = find_first_common_node(link1, link2)
    print(res.val)
    print(res.next)












    