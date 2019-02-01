# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or k == 1:
            return head
        
        t = head
        for i in range(k - 1):
            t = t.next
            if t == None:
                return head
        tmp = head
        tmpNext = tmp.next
        while tmpNext != t:
            p = tmpNext.next
            tmpNext.next = tmp
            tmp = tmpNext
            tmpNext = p
            p = p.next
        head.next = t.next
        t.next = tmp
        while True:
            t1 = head.next
            if t1 == None:
                return t
            for i in range(k - 1):
                t1 = t1.next
                if t1 == None:
                    return t
            tmpHead = head
            head = head.next
            tmp = head
            tmpNext = tmp.next
            while tmpNext != t1:
                p = tmpNext.next
                tmpNext.next = tmp
                tmp = tmpNext
                tmpNext = p
                p = p.next
            head.next = t1.next
            t1.next = tmp
            tmpHead.next = t1
        return t
