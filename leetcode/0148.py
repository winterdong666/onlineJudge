# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def helper(head, lens):
            if lens == 0:
                return None
            if lens == 1:
                head.next = None
                return head
            m = lens // 2
            p = head
            tail = p
            for i in range(m - 1):
                tail = p
                p = p.next
            tail = p
            p = p.next
            tail.next = None
            head1 = helper(head, m)
            head2 = helper(p, lens - m)
            res = ListNode(0)
            p1, p2 = head1, head2
            p = res
            while p1 != None and p2 != None:
                if p1.val < p2.val:
                    p.next = p1
                    p1 = p1.next
                    p = p.next
                else:
                    p.next = p2
                    p2 = p2.next
                    p = p.next
            if p1 == None:
                p.next = p2
            if p2 == None:
                p.next = p1
            res = res.next
            return res
        if head == None:
            return None
        count = 1
        p = head
        while p.next != None:
            p = p.next
            count += 1
        return helper(head, count)
