
def toListNode(numbers):

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        res = True
        lst = []
        try:
            while head.next:
                lst.append(head.val)
                head = head.next
            lst.append(head.val)
            for i in range(int(len(lst)/2)):
                if lst[i] == lst[-1-i]:
                    continue
                else:
                    res = False
                    break
        except AttributeError as e:
            return res
        return res


if __name__ == '__main__':
    so = Solution()
    assert so.isPalindrome(toListNode([1, 2])) == False
    assert so.isPalindrome(toListNode([1, 2, 1])) == True
    assert so.isPalindrome(toListNode([])) == True
    assert so.isPalindrome(toListNode([1])) == True
    assert so.isPalindrome(toListNode([1, 1])) == True
