# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(root):
            if root == None:
                return []
            res = [root.val]
            res1 = helper(root.left)
            res2 = helper(root.right)
            return res + res1 + res2
        return helper(root)
