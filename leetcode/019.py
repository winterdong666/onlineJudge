# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p, q = head, head
        for i in range(n - 1):
            p = p.next
        if p.next == None:
            return head.next
        while p.next.next != None:
            p = p.next
            q = q.next
        q.next = q.next.next
        return head
