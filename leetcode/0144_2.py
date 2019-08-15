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
        DFS = []
        res = []
        if root == None:
            return res
        DFS.append(root)
        while len(DFS) > 0:
            tmp = DFS.pop()
            res.append(tmp.val)
            if tmp.right != None:
                DFS.append(tmp.right)
            if tmp.left != None:
                DFS.append(tmp.left)
        return res
