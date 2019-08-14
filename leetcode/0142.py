# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return None
        start, slow, fast = head, head.next, head.next.next
        while True:
            if fast == None or fast.next == None:
                return None
            if fast == slow:
                while start != slow:
                    start = start.next
                    slow = slow.next
                return start
            fast = fast.next.next
            slow = slow.next
