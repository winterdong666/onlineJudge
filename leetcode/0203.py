# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head != None and head.val == val:
            head = head.next
        if head == None:
            return None
        p, q = head, head.next
        while q != None:
            tmp = q.next
            if q.val == val:
                p.next = tmp
                q = tmp
            else:
                p = q
                q = tmp
        return head
