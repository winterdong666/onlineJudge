# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        res = []
        def inorderHelper(res, root):
            if root == None:
                return
            inorderHelper(res, root.left)
            res.append(root.val)
            inorderHelper(res, root.right)
        inorderHelper(res, root)
        return res
