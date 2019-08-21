# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution:
    def recoverTree(self, root: 'TreeNode') -> 'None':
        """
        Do not return anything, modify root in-place instead.
        """
        first = None
        second = None
        prev = TreeNode(-2147483648)
        if root == None:
            return
        if root.left == None and root.right == None:
            return
        def traverse(root, first, second, prev):
            if root == None:
                return first, second, prev
            first, second, prev = traverse(root.left, first, second, prev)
            if first == None and prev.val >= root.val:
                first = prev
            if first != None and prev.val >= root.val:
                second = root
            prev = root
            first, second, prev = traverse(root.right, first, second, prev)
            return first, second, prev
        first, second, prev = traverse(root, first, second, prev)
        tmp = first.val
        first.val = second.val
        second.val = tmp
