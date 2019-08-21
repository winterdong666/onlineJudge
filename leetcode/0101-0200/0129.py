# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def helper(root):
            if root == None:
                return []
            if root.left == None and root.right == None:
                return [str(root.val)]
            arrayL = helper(root.left)
            arrayR = helper(root.right)
            res = []
            for i in arrayL + arrayR:
                i = str(root.val) + i
                res.append(i)
            return res
        if root == None:
            return 0
        arr = helper(root)
        res = 0
        for i in arr:
            res += int(i)
        return res
