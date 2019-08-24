# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root, p, q):
            if root == None:
                return None
            if root.val == p.val or root.val == q.val:
                return root
            elif (root.val - p.val) * (root.val - q.val) < 0:
                return root
            else:
                if root.val < p.val:
                    return helper(root.right, p, q)
                else:
                    return helper(root.left, p, q)
        return helper(root, p, q)
