# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: 'ListNode', x: 'int') -> 'ListNode':
        head1 = ListNode(0)
        head2 = ListNode(0)
        p1 = head1
        p2 = head2
        p = head
        while p != None:
            tmp = p
            p = p.next
            if tmp.val < x:
                p1.next = tmp
                p1 = tmp
            else:
                p2.next = tmp
                p2 = tmp
        p2.next = None
        p1.next = head2.next
        return head1.next
