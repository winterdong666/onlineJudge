# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: 'TreeNode') -> 'bool':
        if root == None:
            return True
        def judgeHelper(l, r):
            if l == None and r == None:
                return True
            if l == None or r == None:
                return False
            if l.val != r.val:
                return False
            return judgeHelper(l.left, r.right) and judgeHelper(l.right, r.left)
        return judgeHelper(root.left, root.right)
