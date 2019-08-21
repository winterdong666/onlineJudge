# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> 'TreeNode':
        def helper(preorder, inorder):
            if preorder == []:
                return None
            root = TreeNode(preorder[0])
            i = 0
            while inorder[i] != preorder[0]:
                i += 1
            root.left = helper(preorder[1: i + 1], inorder[:i])
            root.right = helper(preorder[i + 1:], inorder[i + 1:])
            return root
        return helper(preorder, inorder)
