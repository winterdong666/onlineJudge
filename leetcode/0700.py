# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def helper(root, val):
            if root == None:
                return None
            elif root.val == val:
                return root
            elif root.val > val:
                return helper(root.left, val)
            else:
                return helper(root.right, val)
        return helper(root, val)
