"""
面试题 35：复杂链表的复制
题目：请实现函数 ComplexListNode* Clone (ComplexListNode* pHead)，复
制一个复杂链表。在复杂链表中，每个结点除了有一个 m_pNext 指针指向下一个
结点外，还有一个 m_pSibling 指向链表中的任意结点或者 nullptr。

"""


class ComplexNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.sibling = None


def connect_nodes(node: ComplexNode,
                  nxt: ComplexNode, 
                  sibling: ComplexNode) -> ComplexNode:
    if node:
        node.next = nxt
        node.sibling = sibling

def print_list(node: ComplexNode):
    res = []
    root = node
    while root:
        print("the value of the node is: ", root.val)
        res.append(root.val)
        if root.sibling:
            print("the value of its sibling is: ", root.sibling.val)
            res.append(root.sibling.val)
        else:
            print("the node does not have a sibling")
            res.append(None)
        root = root.next
    return res



def clone_list_nodes_with_dict(head: ComplexNode) -> ComplexNode:
    """
    Clone a given complex nodes.

    Parameters
    -----------
    head: the given Complex Nodes.

    Returns
    ---------
    out: the cloned Complex Nodes of the given one.

    Notes
    ------

    """
    if not head:
        return None
    
    sib_dict = {}

    new = ComplexNode(head.val)
    new.sibling = head.sibling

    node = new
    while head.next:
        node.next = ComplexNode(head.next.val)
        if head.sibling:
            sib_dict[head.val] = head.sibling.val
            # node.sibling = ComplexNode(head.sibling.val)
        else:
            sib_dict[head.val] = None
            # node.sibling = None
        node = node.next
        head = head.next
    
    node = new
    while node.next:
        node.sibling = ComplexNode(sib_dict[node.val])
        node = node.next
    
    return new


def clone_list_nodes(head: ComplexNode) -> ComplexNode:

    if not head:
        return None
    cloned = clone_nodes(head)
    connected = connect_sibling_nodes(cloned)
    clone_head = reconnect_nodes(connected)
    return clone_head
    

def clone_nodes(head: ComplexNode) -> ComplexNode:
    node = head
    while node:
        clone = ComplexNode(node.val)
        clone.next = node.next
        clone.sibling = None

        node.next = clone
        node = clone.next
    return head

def connect_sibling_nodes(head: ComplexNode) -> ComplexNode:
    node = head
    while node:
        clone = node.next
        if node.sibling:
            clone.sibling = node.sibling.next
        node = clone.next
    return head

def reconnect_nodes(head: ComplexNode) -> ComplexNode:
    node = head
    clone_head, clone_node = None, None
    if node:
        clone_head = clone_node = node.next
        node.next = clone_node.next
        node = node.next
    while node:
        clone_node.next = node.next
        clone_node = clone_node.next
        node.next = clone_node.next
        node = node.next
    return clone_head



if __name__ == '__main__':
    root = ComplexNode("A")
    b = ComplexNode("B")
    c = ComplexNode("C")
    d = ComplexNode("D")
    e = ComplexNode("E")

    # connect_nodes(root, b, c)
    # connect_nodes(root.next, c, e)
    # connect_nodes(root.next.next, d, None)
    # connect_nodes(root.next.next.next, e, b)

    connect_nodes(root, b, c)
    connect_nodes(b, c, e)
    connect_nodes(c, d, None)
    connect_nodes(d, e, b)
    res = print_list(root)
    print(res)

    new = clone_list_nodes_with_dict(root)
    res = print_list(new)
    print(res)


    a = ComplexNode(1)
    connect_nodes(a, None, a)
    lst = print_list(a)
    print(lst)

    res = clone_list_nodes_with_dict(a)
    print(print_list(res))




    a = None
    lst = print_list(a)
    res = clone_list_nodes(a)
    print(res)

    res = clone_list_nodes_with_dict(a)
    print(res)


