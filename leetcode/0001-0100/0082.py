# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':
        res = ListNode(0)
        if head == None:
            return head
        resList = [head.val]
        p = head
        q = p.next
        while q != None:
            if q.val == p.val and resList != [] and q.val == resList[-1]:
                resList.pop()
            if q.val != p.val:
                resList.append(q.val)
            p = p.next
            q = p.next
        t = res
        for i in resList:
            t.next = ListNode(i)
            t = t.next
        return res.next
