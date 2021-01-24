class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def get_num(l):
            llist = []
            while l:
                llist.append(l.val)
                l = l.next
            num = sum([n*10**i for (i,n) in enumerate(llist)])
            return num
        added = str(get_num(l1) + get_num(l2))
        lsum = [added[i] for i in range(len(added))]
        dummy = end = ListNode(0)
        for k in [int(i) for i in lsum[::-1]]:
            end.next = end = ListNode(k)
        return dummy.next