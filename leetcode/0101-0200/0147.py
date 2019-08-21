# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        newHead = head
        p, q = head.next, head.next.next
        tail = head
        count = 1
        while p != None:
            if newHead.val >= p.val:
                p.next = newHead
                newHead = p
            else:
                tmp = newHead
                last = newHead
                tmpCount = 0
                while tmp.val < p.val and tmpCount < count:
                    last = tmp
                    tmp = tmp.next
                    tmpCount += 1
                if tmpCount == count:
                    tail = p
                    last.next = p
                else:
                    last.next = p
                    p.next = tmp
            tail.next = q
            p = q
            if q != None:
                q = q.next
            count += 1
        return newHead
