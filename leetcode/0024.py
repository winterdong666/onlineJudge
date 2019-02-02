# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        t = head.next
        head.next = t.next
        t.next = head
        
        r = t.next.next
        p = t.next
        while r != None and r.next != None:
            tmp = r.next
            p.next = tmp
            r.next = tmp.next
            tmp.next = r
            p = r
            r = r.next
        return t
