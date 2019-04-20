# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    forwardTraverse = []
        
    def __init__(self, root: TreeNode):  
        tmparr = []
        def traverse(root, arr):
            if root == None:
                return
            traverse(root.left, arr)
            arr.append(root.val)
            traverse(root.right, arr)
        traverse(root, tmparr)
        self.forwardTraverse = tmparr[:]

    def next(self) -> int:
        """
        @return the next smallest number
        """
        t = self.forwardTraverse[0]
        self.forwardTraverse = self.forwardTraverse[1:]
        return t
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.forwardTraverse != []


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
