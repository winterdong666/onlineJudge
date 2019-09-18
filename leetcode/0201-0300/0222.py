# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def judgeFull(root):
            count = 0
            if root == None:
                return True, count
            l, r = root.left, root.right
            while l != None and r != None:
                l = l.left
                r = r.right
                count += 1
            if l == None and r == None:
                return True, count
            else:
                return False, count + 1
        def helper(root):
            if root == None:
                return 0
            flag, layer = judgeFull(root)
            if flag:
                count = 2
                for i in range(layer):
                    count *= 2
                return count - 1
            else:
                flag2, layer2 = judgeFull(root.left)
                if flag2:
                    count = 2
                    for i in range(layer2):
                        count *= 2
                    return count + helper(root.right)
                else:
                    layer2 -= 1
                    count = 2
                    for i in range(layer2):
                        count *= 2
                    return count + helper(root.left)
        return helper(root)
                
