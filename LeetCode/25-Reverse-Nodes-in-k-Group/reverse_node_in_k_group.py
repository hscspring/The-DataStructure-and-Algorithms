# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self):
        self.last_half = None

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        i = 0
        j = i + k
        length = 0
        ct = head
        while ct:
            length += 1
            ct = ct.next
        while j < length + 1:
            head = self.reverse_between(head, i, j)
            i = j
            j = i + k
        return head

    def reverse_between(self, head: ListNode, i: int, j: int) -> ListNode:
        ln = head
        k = 0
        pt = None
        while ln and k < i:
            pt = ln
            ln = ln.next
            k += 1
        lt = self.reverse_n(ln, j - i)
        if pt:
            pt.next = lt
            return head
        else:
            return lt

    def reverse_between2(self, head: ListNode, i: int, j: int) -> ListNode:
        if i == 1:
            return self.reverse_n(head, j)
        head.next = self.reverse_between2(head.next, i - 1, j - 1)
        return head





    def reverseKGroup2(self, head: ListNode, k: int) -> ListNode:
        a = head
        b = head
        for i in range(k):
            if not b:
                return head
            b = b.next
        new_head = self.reverse_between3(a, b)
        a.next = self.reverseKGroup2(b, k)
        return new_head

    def reverse_between3(self, a: ListNode, b: ListNode) -> ListNode:
        pre = None
        curr = a
        while curr != b:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt
        return pre



    def reverse_n(self, head: ListNode, n: int) -> ListNode:
        if n == 1:
            self.last_half = head.next
            return head
        last = self.reverse_n(head.next, n-1)
        head.next.next = head
        head.next = self.last_half
        return last

    
    def reverse(self, head: ListNode) -> ListNode:
        if not head.next:
            return head
        last = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return last

    def reverse2(self, head: ListNode) -> ListNode:
        pre = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt
        return pre

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
l4 = so.build([1, 2, 3, 4, 5, 6])
so.print(l1)
so.print(l2)
so.print(l3)


print("reverse")
l4 = so.build([1, 2, 3, 4, 5, 6])
res = so.reverse(l4)
so.print(res)
l4 = so.build([1, 2, 3, 4, 5, 6])
res = so.reverse2(l4)
so.print(res)


print("reverse_n")
l4 = so.build([1, 2, 3, 4, 5, 6])
res = so.reverse_n(l4, 2)
so.print(res)

print("reverse_between")
l4 = so.build([1, 2, 3, 4, 5, 6])
res = so.reverse_between(l4, 0, 2)
so.print(res)

print("reverse_between2")
l4 = so.build([1, 2, 3, 4, 5, 6])
res = so.reverse_between2(l4, 1, 2)
so.print(res)

print("reverseKGroup")
l4 = so.build([1, 2, 3, 4, 5, 6])
res = so.reverseKGroup(l4, 3)
so.print(res)
l4 = so.build([1, 2, 3, 4, 5, 6])
res = so.reverseKGroup(l4, 2)
so.print(res)

print("reverseKGroup2")
l4 = so.build([1, 2, 3, 4, 5, 6])
res = so.reverseKGroup2(l4, 3)
so.print(res)
l4 = so.build([1, 2, 3, 4, 5, 6])
res = so.reverseKGroup2(l4, 2)
so.print(res)



