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
        if root == None:
            return
        root.next == None
        if root.left == None and root.right == None:
            return
        tmp = root
        while True:
            p = tmp
            q = None
            while p != None and p.left == None and p.right == None:
                p = p.next
            if p == None:
                return
            if p.left == None:
                q = p.right
                tmp = q
            elif p.right != None:
                p.left.next = p.right
                q = p.right
                tmp = p.left
            else:
                q = p.left
                tmp = q
            while p != None:
                if p.left != None and p.right != None:
                    q.next = p.left
                    p.left.next = p.right
                    q = p.right
                elif p.left != None:
                    q.next = p.left
                    q = p.left
                elif p.right != None:
                    q.next = p.right
                    q = p.right
                p = p.next
            q.next = None
            
