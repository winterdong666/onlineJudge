# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def getLen(head):
            if head == None:
                return 0
            count = 1
            p = head.next
            while p != None:
                count += 1
                p = p.next
            return count
        
        if headA == None or headB == None:
            return None
        lA = getLen(headA)
        lB = getLen(headB)
        pA, pB = headA, headB
        while lA > lB:
            pA = pA.next
            lA -= 1
        while lB > lA:
            pB = pB.next
            lB -= 1
        while pA != None:
            if pA == pB:
                return pA
            else:
                pA = pA.next
                pB = pB.next
        return None
