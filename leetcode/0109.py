# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: 'ListNode') -> 'TreeNode':
        def count(head):
            p = head
            res = 0
            while p != None:
                p = p.next
                res += 1
            return res
        def helper(listNode, n):
            if n == 0:
                return None, listNode
            root = TreeNode(0)
            root.left, listNode = helper(listNode, n // 2)
            root.val = listNode.val
            listNode = listNode.next
            root.right, listNode = helper(listNode, n - n // 2 - 1)
            return root, listNode
        root, p = None, None
        root, p = helper(head, count(head))
        return root
