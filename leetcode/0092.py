# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: 'ListNode', m: 'int', n: 'int') -> 'ListNode':
        if m == n:
            return head
        if m == 1:
            p = head
            q = None
            for i in range(n - 1):
                tmp = p.next
                p.next = q
                q = p
                p = tmp
            head.next = p.next
            p.next = q
            return p
        else:
            p = head
            for i in range(m - 2):
                p = p.next
            tmp = p
            tmp2 = p.next
            p = p.next.next
            q = tmp.next
            for i in range(n - m - 1):
                tmp3 = p.next
                p.next = q
                q = p
                p = tmp3
            tmp3 = p.next
            p.next = q
            tmp.next = p
            tmp2.next = tmp3
            return head
            
            
