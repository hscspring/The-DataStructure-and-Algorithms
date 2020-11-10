from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:

    val: int
    next = None


def print_link_list(head: Node):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)


def connect_to_link_list(lst: list) -> Node:
    head = Node(None)
    node = head
    for i in lst:
        tmp = Node(i)
        node.next = tmp
        node = node.next
    return head.next


def reverse_linklist(head: Node) -> Node:
    prev = None
    while head:
        tmp = head.next
        head.next = prev
        prev = head
        head = tmp
    return prev


def reverse_linklist_between_two_nodes(head: Node, start: Node, end: Node) -> Node:
    prev = None
    curr = start
    while curr and curr != end:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    return head



def reverse_linklist_from_two_nodes(head: Node, start: int, end: int) -> Node:
    node = head
    i = 0
    prev = None
    while node:
        if i < start:
            node = node.next
            prev = node
            continue
        if i > end:
            break
        tmp = node.next

        i += 1


def reverse_k_nodes(head: Node, k: int) -> Node:
    i = 0
    idx = 0
    link = head
    while head:
        if i % k == 0:
            start = idx
        if i < k:
            i += 1
        if i == k:
            i = 0
            end = idx
            link = reverse_linklist_from_two_nodes(link, start, end)
        head = head.next
        idx += 1


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    head = connect_to_link_list(lst)
    print_link_list(head)
    # rhead = reverse_linklist(head)
    # print(rhead)
    # print_link_list(rhead)

    interval_head = reverse_linklist_between_two_nodes(head, Node(1), Node(3))
    print_link_list(interval_head)


