# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: 'List[int]', postorder: 'List[int]') -> 'TreeNode':
        if postorder == []:
            return None
        root = TreeNode(postorder.pop())
        v = root.val
        ind = inorder.index(v)
        root.left = self.buildTree(inorder[:ind], postorder[:ind])
        root.right = self.buildTree(inorder[ind + 1:], postorder[ind:])
        return root
