"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        def helper(t1, t2):
            tl, tr, bl, br = None, None, None, None
            if (t1.topLeft.isLeaf == True and t1.topLeft.val == True) or (t2.topLeft.isLeaf == True and t2.topLeft.val == True):
                tl = Node(True, True, None, None, None, None)
            elif (t1.topLeft.isLeaf == True and t1.topLeft.val == False):
                tl = Node(t2.topLeft.val, t2.topLeft.isLeaf, t2.topLeft.topLeft, t2.topLeft.topRight, t2.topLeft.bottomLeft, t2.topLeft.bottomRight)
            elif (t2.topLeft.isLeaf == True and t2.topLeft.val == False):
                tl = Node(t1.topLeft.val, t1.topLeft.isLeaf, t1.topLeft.topLeft, t1.topLeft.topRight, t1.topLeft.bottomLeft, t1.topLeft.bottomRight)
            else:
                tl = helper(t1.topLeft, t2.topLeft)
                
            if (t1.topRight.isLeaf == True and t1.topRight.val == True) or (t2.topRight.isLeaf == True and t2.topRight.val == True):
                tr = Node(True, True, None, None, None, None)
            elif (t1.topRight.isLeaf == True and t1.topRight.val == False):
                tr = Node(t2.topRight.val, t2.topRight.isLeaf, t2.topRight.topLeft, t2.topRight.topRight, t2.topRight.bottomLeft, t2.topRight.bottomRight)
            elif (t2.topRight.isLeaf == True and t2.topRight.val == False):
                tr = Node(t1.topRight.val, t1.topRight.isLeaf, t1.topRight.topLeft, t1.topRight.topRight, t1.topRight.bottomLeft, t1.topRight.bottomRight)
            else:
                tr = helper(t1.topRight, t2.topRight)
                
            if (t1.bottomLeft.isLeaf == True and t1.bottomLeft.val == True) or (t2.bottomLeft.isLeaf == True and t2.bottomLeft.val == True):
                bl = Node(True, True, None, None, None, None)
            elif (t1.bottomLeft.isLeaf == True and t1.bottomLeft.val == False):
                bl = Node(t2.bottomLeft.val, t2.bottomLeft.isLeaf, t2.bottomLeft.topLeft, t2.bottomLeft.topRight, t2.bottomLeft.bottomLeft, t2.bottomLeft.bottomRight)
            elif (t2.bottomLeft.isLeaf == True and t2.bottomLeft.val == False):
                bl = Node(t1.bottomLeft.val, t1.bottomLeft.isLeaf, t1.bottomLeft.topLeft, t1.bottomLeft.topRight, t1.bottomLeft.bottomLeft, t1.bottomLeft.bottomRight)
            else:
                bl = helper(t1.bottomLeft, t2.bottomLeft)
            
            if (t1.bottomRight.isLeaf == True and t1.bottomRight.val == True) or (t2.bottomRight.isLeaf == True and t2.bottomRight.val == True):
                br = Node(True, True, None, None, None, None)
            elif (t1.bottomRight.isLeaf == True and t1.bottomRight.val == False):
                br = Node(t2.bottomRight.val, t2.bottomRight.isLeaf, t2.bottomRight.topLeft, t2.bottomRight.topRight, t2.bottomRight.bottomLeft, t2.bottomRight.bottomRight)
            elif (t2.bottomRight.isLeaf == True and t2.bottomRight.val == False):
                br = Node(t1.bottomRight.val, t1.bottomRight.isLeaf, t1.bottomRight.topLeft, t1.bottomRight.topRight, t1.bottomRight.bottomLeft, t1.bottomRight.bottomRight)
            else:
                br = helper(t1.bottomRight, t2.bottomRight)
            
            return Node(t1.val or t2.val, False, tl, tr, bl, br)
        
        def merge(t):
            if t.isLeaf:
                return t
            else:
                t.topLeft = merge(t.topLeft)
                t.topRight = merge(t.topRight)
                t.bottomLeft = merge(t.bottomLeft)
                t.bottomRight = merge(t.bottomRight)
                if (t.topLeft.isLeaf == True and t.topLeft.val == True) and (t.topRight.isLeaf == True and t.topRight.val == True) and (t.bottomLeft.isLeaf == True and t.bottomLeft.val == True) and (t.bottomRight.isLeaf == True and t.bottomRight.val == True):
                    t = Node(True, True , None, None, None, None)
                elif (t.topLeft.isLeaf == True and t.topLeft.val == False) and (t.topRight.isLeaf == True and t.topRight.val == False) and (t.bottomLeft.isLeaf == True and t.bottomLeft.val == False) and (t.bottomRight.isLeaf == True and t.bottomRight.val == False):
                    t = Node(False, True, None, None, None, None)
                return t
        
        res = None
        if (quadTree1.isLeaf == True and quadTree1.val == True) or (quadTree2.isLeaf == True and quadTree2.val == True):
            res =  Node(True, True, None, None, None, None)
        elif (quadTree1.isLeaf == True and quadTree1.val == False):
            res = quadTree2
        elif (quadTree2.isLeaf == True and quadTree2.val == False):
            res = quadTree1
        else:
            res = helper(quadTree1, quadTree2)
        return merge(res)
        
