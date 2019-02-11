# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        def isValidHelper(root, minNum, maxNum):
            if root == None:
                return True
            if root.val <= minNum or root.val >= maxNum:
                return False
            return isValidHelper(root.left, minNum, root.val) and isValidHelper(root.right, root.val, maxNum)
        return isValidHelper(root, -2147483649, 2147483648)
