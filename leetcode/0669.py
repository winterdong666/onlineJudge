# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        def helper(root, l, r):
            if root == None:
                return root
            if root.val > r:
                return helper(root.left, l, r)
            if root.val < l:
                return helper(root.right, l, r)
            root.left = helper(root.left, l, r)
            root.right = helper(root.right, l, r)
            return root
        return helper(root, L, R)
