class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(head: ListNode) -> ListNode:
    pre = None
    cur = head
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre

if __name__ == '__main__':

    inp = [1,2,3,4,5]
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in inp:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    rev = reverseList(ptr)
    while rev:
        print(rev.val)
        rev = rev.next