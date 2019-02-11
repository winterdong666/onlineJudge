# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def findMax(root):
    if root.left == None and root.right == None:
        return root.val
    t1 = -2147483648
    t2 = -2147483648
    if root.left != None:
        t1 = findMax(root.left)
    if root.right != None:
        t2 = findMax(root.right)
    return max(t1, t2, root.val)

def findMin(root):
    if root.left == None and root.right == None:
        return root.val
    t1 = 2147483647
    t2 = 2147483647
    if root.left != None:
        t1 = findMin(root.left)
    if root.right != None:
        t2 = findMin(root.right)
    return min(t1, t2, root.val)

class Solution:
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        if root == None:
            return True
        if root.left != None and findMax(root.left) >= root.val:
            return False
        if root.right != None and findMin(root.right) <= root.val:
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)
