# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        p, q = head, head.next
        while q != None:
            tmp = q.next
            q.next = p
            p = q
            q = tmp
        head.next = None
        return p
