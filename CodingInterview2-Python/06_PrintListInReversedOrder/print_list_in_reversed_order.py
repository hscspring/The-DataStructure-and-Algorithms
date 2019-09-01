"""
面试题 6：从尾到头打印链表
题目：输入一个链表的头结点，从尾到头反过来打印出每个结点的值。

"""

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def print_list_reverse(node) -> list:
    """
    print_list_reverse(Node)
    
    Print a linklist reversedly.

    Parameters
    -----------
    Node: Node

    Returns
    -------
    out: list
    """
    res, stack = [], []
    while node:
        stack.append(node.val)
        node = node.next
    while len(stack):
        res.append(stack.pop())
    return res

def print_list_reverse_recursive(node, res) -> list:
    if node:
        res.insert(0, node.val)
        print_list_reverse_recursive(node.next, res)


def lst2link(lst):
    root = Node(None)
    ptr = root
    for i in lst:
        ptr.next = Node(i)
        ptr = ptr.next
    ptr = root.next
    return ptr

if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    # lst = [1]
    node = lst2link(lst)
    # while node:
    #     print(node.val)
    #     node = node.next
    res = []
    print_list_reverse_recursive(node, res)
    print(res)
