# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: 'TreeNode') -> 'bool':
        def helper(root):
            if root == None:
                return True, 0
            flag1, d1 = helper(root.left)
            if flag1 == False:
                return False, -1
            flag2, d2 = helper(root.right)
            if flag2 == False:
                return False, -1
            if abs(d1 - d2) > 1:
                return False, -1
            return True, max(d1, d2) + 1
        flag = False
        d = 0
        flag, d = helper(root)
        return flag
