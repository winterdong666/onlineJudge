# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':
        if head == None:
            return head
        p = head
        q = head.next
        while q != None:
            if q.val == p.val:
                p.next = q.next
                q = q.next
            else:
                p = p.next
                q = q.next
        return head
