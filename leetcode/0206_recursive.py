# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def helper(head):
            if head == None or head.next == None:
                return
            helper(head.next)
            head.next.next = head
        if head == None:
            return None
        tail = head
        while tail.next != None:
            tail = tail.next
        helper(head)
        head.next = None
        return tail
