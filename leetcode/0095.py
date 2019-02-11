# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: 'int') -> 'List[TreeNode]':
        def generateHelper(s, e):
            res = []
            if s > e:
                return [None]
            if s == e:
                return [TreeNode(s)]
            for i in range(s, e + 1):
                left = generateHelper(s, i - 1)
                right = generateHelper(i + 1, e)
                for m in left:
                    for n in right:
                        root = TreeNode(i)
                        root.left = m
                        root.right = n
                        res.append(root)
            return res
        if n == 0:
            return []
        return generateHelper(1, n)
                        
