# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        p = head
        q = None
        count = 0
        while p != None:
            q = p
            p = p.next
            count += 1
        
        c = (count - k % count) % count
        if c == 0:
            return head
        q.next = head
        p = head
        for i in range(c):
            q = p
            p = p.next
        q.next = None
        return p
