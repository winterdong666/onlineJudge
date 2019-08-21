# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        def findLen(head):
            if head == None:
                return 0
            p = head
            res = 1
            while p.next != None:
                p = p.next
                res += 1
            return res
        def splitLink(head, l):
            m = (l - 1) // 2 + 1
            count = 1
            p = head
            while count < m:
                count += 1
                p = p.next
            q = p.next
            p.next = None
            return q
        def reverseLink(head):
            if head == None:
                return head
            if head.next == None:
                return head
            p, q, r = head, head.next, head.next.next
            while r != None:
                q.next = p
                p = q
                q = r
                r = r.next
            q.next = p
            head.next = None
            return q
        def mergeLink(head, head2):
            p, p2 = head, head2
            while p2 != None:
                tmp = p.next
                tmp2 = p2.next
                p.next = p2
                p2.next = tmp
                p = tmp
                p2 = tmp2
        if head == None or head.next == None:
            return
        l = findLen(head)
        mid = splitLink(head, l)
        head2 = reverseLink(mid)
        mergeLink(head, head2)
