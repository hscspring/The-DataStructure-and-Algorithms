class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def swapPairs3(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        node = ListNode(0)
        tmp = node
        i = 0
        while head:
            if i%2 == 0:
                if head.next:
                    tmp.next = ListNode(head.next.val)
                    tmp.next.next = ListNode(head.val)
                else:
                    tmp.next = ListNode(head.val)
            tmp = tmp.next
            head = head.next
            i += 1
        return node.next
    
    def swapPairs2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        new_head = head.next
        head.next = self.swapPairs2(head.next.next)
        new_head.next = head
        return new_head
    
    def swapPairs1(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        node = ListNode(0)
        node.next = head
        prev = node
        curr = head
        while curr and curr.next:
            prev.next = curr.next
            curr.next = curr.next.next
            prev.next.next = curr
            prev = curr
            curr = curr.next
        return node.next