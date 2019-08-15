# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        DFS = []
        roots = []
        res = []
        DFS.append(root)
        while len(DFS) > 0:
            tmp = DFS.pop()
            if len(roots) == 0 or roots[-1] != tmp:
                DFS.append(tmp)
                roots.append(tmp)
                if tmp.right != None:
                    DFS.append(tmp.right)
                if tmp.left != None:
                    DFS.append(tmp.left)
            else:
                roots.pop()
                res.append(tmp.val)
        return res
