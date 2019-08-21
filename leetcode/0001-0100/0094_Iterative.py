# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        stack = []
        status = [] #0 means unused, 1 means using
        res = []
        if root == None:
            return []
        stack.append(root)
        status.append(0)
        while len(stack) > 0:
            tmp = stack.pop()
            tmpState = status.pop()
            if tmpState == 0:
                stack.append(tmp)
                status.append(1)
                if tmp.left != None:
                    stack.append(tmp.left)
                    status.append(0)
            else:
                res.append(tmp.val)
                if tmp.right != None:
                    stack.append(tmp.right)
                    status.append(0)
        return res
