"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def helper(root):
            res = []
            if root == None:
                return res
            for i in root.children:
                res = res + helper(i)
            res.append(root.val)
            return res
        return helper(root)
