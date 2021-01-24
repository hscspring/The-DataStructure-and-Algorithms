# Definition for singly-linked list.
from functools import wraps
import time
from typing import List

def timethis(func):
    @wraps(func)
    def wapper(self, *args, **kwargs):
        start = time.time()
        res = func(self, *args, **kwargs)
        end = time.time()
        print("cost time: ", end - start)
        return res
    return wapper

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    @timethis
    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        else:
            mid = len(lists) // 2
            l = self.mergeKLists2(lists[:mid])
            r = self.mergeKLists2(lists[mid:])
            return self.mergeKLists2([l, r])


    @timethis
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            i = 1
            l1 = lists[0]
            while i < len(lists):
                l2 = lists[i]
                l1 = self.mergeTwoLists(l1, l2)
                i += 1
        return l1


    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        lt = ListNode()
        if l1 and not l2:
            return l1
        if l2 and not l1:
            return l2
        if not l1 or not l2:
            return lt.next
        root = lt
        while l1 and l2:
            while l1 and l2 and l1.val <= l2.val:
                root.next = ListNode(l1.val)
                l1 = l1.next
                root = root.next
            while l1 and l2 and l2.val <= l1.val:
                root.next = ListNode(l2.val)
                l2 = l2.next
                root = root.next
        while l1:
            root.next = ListNode(l1.val)
            l1 = l1.next
            root = root.next
        while l2:
            root.next = ListNode(l2.val)
            l2 = l2.next
            root = root.next
        return lt.next

    def build(self, lst: list) -> ListNode:
        root = ListNode()
        lt = root
        for i in lst:
            lt.next = ListNode(i)
            lt = lt.next
        return root.next

    def print(self, lt: ListNode) -> list:
        plt = lt
        res = []
        while plt:
            res.append(plt.val)
            plt = plt.next
        print(res)


so = Solution()
l1 = so.build([1, 2, 4])
l2 = so.build([1, 3, 4])
l3 = so.build([0, 2, 5])
l4 = so.build([1])
so.print(l1)
so.print(l2)
so.print(l3)

print("="* 20)
lt = so.mergeKLists([l1, l2, l3])
so.print(lt)

lt2 = so.mergeKLists2([l1, l2, l3])
so.print(lt2)
print("="* 20)

so.print(so.mergeKLists([]))
so.print(so.mergeKLists([[]]))
so.print(so.mergeKLists([l4]))
