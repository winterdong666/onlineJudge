# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def merge2Lists(lists, i, j):
            res = ListNode(0)
            tmp = res
            p = lists[i]
            q = lists[j]
            while p != None and q != None:
                if p.val <= q.val:
                    tmp.next = ListNode(p.val)
                    p = p.next
                else:
                    tmp.next = ListNode(q.val)
                    q = q.next
                tmp = tmp.next
            if p != None:
                tmp.next = p
            if q != None:
                tmp.next = q
            return res.next
        if lists == []:
            return lists
        if len(lists) == 1:
            return lists[0]
        t = 1
        m = 2
        while m < len(lists):
            m = m * 2
            t = t + 1
        res = lists
        while len(res) > 1:
            tmp = []
            for i in range(0, len(res) - 1, 2):
                tmp.append(merge2Lists(res, i, i + 1))
            if len(res) % 2 == 1:
                tmp.append(res[-1])
            res = tmp
        return res[0]
        
