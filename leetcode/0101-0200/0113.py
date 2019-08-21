# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: 'TreeNode', sum: 'int') -> 'List[List[int]]':
        def helper(root, sum):
            if root == None:
                return []
            if root.left == None and root.right == None:
                if root.val == sum:
                    return [[root.val]]
                else:
                    return []
            res = []
            res1 = []
            res2 = []
            res1 = helper(root.left, sum - root.val)
            res2 = helper(root.right, sum - root.val)
            for i in res1:
                tmp = i[:]
                tmp.append(root.val)
                res.append(tmp)
            for i in res2:
                tmp = i[:]
                tmp.append(root.val)
                res.append(tmp)
            return res
        res = helper(root, sum)
        for i in range(len(res)):
            res[i] = res[i][::-1]
        return res
