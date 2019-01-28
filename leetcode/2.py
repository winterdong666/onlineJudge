# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode((l1.val + l2.val) % 10)
        jinwei = (int(l1.val) + int(l2.val)) // 10
        tmp1 = l1.next
        tmp2 = l2.next
        tmp3 = res
        while tmp1 != None and tmp2 != None:
            tmp3.next = ListNode((tmp1.val + tmp2.val + jinwei) % 10)
            jinwei = int(tmp1.val + tmp2.val + jinwei) // 10
            tmp3 = tmp3.next
            tmp1 = tmp1.next
            tmp2 = tmp2.next
        while tmp1 != None:
            tmp3.next = ListNode((tmp1.val + jinwei) % 10)
            jinwei = int(tmp1.val + jinwei) // 10
            tmp3 = tmp3.next
            tmp1 = tmp1.next
        while tmp2 != None:
            tmp3.next = ListNode((tmp2.val + jinwei) % 10)
            jinwei = int(tmp2.val + jinwei) // 10
            tmp3 = tmp3.next
            tmp2 = tmp2.next
        if jinwei != 0:
            tmp3.next = ListNode(jinwei)
        return res
