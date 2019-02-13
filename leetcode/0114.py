# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: 'TreeNode') -> 'None':
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return
        p = root
        while p != None:
            if p.left != None:
                q = p.left
                while q.right != None:
                    q = q.right
                q.right = p.right
                p.right = p.left
                p.left = None
            p = p.right
