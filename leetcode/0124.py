# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: 'TreeNode') -> 'int':
        self.res = -2147483648
        def helper(root):
            if root == None:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            self.res = max(self.res, left + root.val + right)
            return max(root.val + max(left, right), 0)
        helper(root)
        return self.res
