# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        if root == None:
            return []
        stack = [root]
        layer = [0]
        res = []
        while len(stack) > 0:
            node = stack.pop()
            nodeLayer = layer.pop()
            if nodeLayer >= len(res):
                res.append([node.val])
            else:
                res[nodeLayer].append(node.val)
            if node.right != None:
                stack.append(node.right)
                layer.append(nodeLayer + 1)
            if node.left != None:
                stack.append(node.left)
                layer.append(nodeLayer + 1)
        for i in range(len(res)):
            if i % 2:
                res[i] = res[i][::-1]
        return res
