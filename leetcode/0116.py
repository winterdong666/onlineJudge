# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        def helper(root):
            if root == None:
                return
            p, q = root.left, root.right
            while p != None:
                p.next = q
                p = p.right
                q = q.left
            helper(root.left)
            helper(root.right)
        if root == None:
            return
        p = root
        p.next = None
        while p.right != None:
            p = p.right
            p.next = None
        helper(root)
