"""
面试题 18（二）：删除链表中重复的结点
题目：在一个排序的链表中，如何删除重复的结点？例如，在图 3.4（a）中重复
结点被删除之后，链表如图 3.4（b）所示。
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

def delete_duplicated_node(root: Node) -> Node:
    """
    Given a link, delete a node in O(1).

    Parameters
    -----------
    root: Node
        link root
    Returns
    ---------
    out: Node
        new link without duplicated node

    Notes
    ------
    
    """
    if not root or not root.next:
        return root
    pprev = None
    pnode = root
    while pnode:
        pnext = pnode.next
        need_delete = False
        if pnext and pnode.val == pnext.val:
            need_delete = True
        
        if not need_delete:
            pprev = pnode
            pnode = pnode.next
        else:
            val = pnode.val
            pdel = pnode
            while pdel and pdel.val == val:
                pnext = pdel.next
                pdel = None
                pdel = pnext
            if not pprev:
                root = pnext
            else:
                pprev.next = pnext
            pnode = pnext
    return root



if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    root = list2link(lst)
    print(link2list(root))




