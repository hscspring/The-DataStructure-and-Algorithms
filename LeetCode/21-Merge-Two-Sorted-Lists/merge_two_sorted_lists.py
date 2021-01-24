# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
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
l1 = so.build([1,2,4])
l2 = so.build([1,3,4])
so.print(l1)
so.print(l2)

lt = so.mergeTwoLists(l1, l2)
so.print(lt)



