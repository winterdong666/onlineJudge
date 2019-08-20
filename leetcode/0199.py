# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        if root == None:
            return res
        DFS = [root]
        usedRight = []
        used = []
        level = 1
        while len(DFS) > 0:
            tmp = DFS.pop()
            if len(usedRight) > 0 and usedRight[-1] == tmp:
                usedRight.pop()
                DFS.append(tmp)
                used.append(tmp)
                if tmp.left != None:
                    DFS.append(tmp.left)
                    level += 1
                continue
            elif len(used) > 0 and used[-1] == tmp:
                used.pop()
                level -= 1
            else:
                if level > len(res):
                    res.append(tmp.val)
                DFS.append(tmp)
                usedRight.append(tmp)
                if tmp.right != None:
                    DFS.append(tmp.right)
                    level += 1
        return res
