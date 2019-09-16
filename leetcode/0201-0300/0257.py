# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def helper(root):
            if root == None:
                return []
            if root.left == None and root.right == None:
                return [str(root.val)]
            l, r, res = helper(root.left), helper(root.right), []
            for i in l + r:
                t = str(root.val) + "->" + i
                res.append(t)
            return res
        return helper(root)
