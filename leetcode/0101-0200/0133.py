"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        node2Index = {node: 0}
        nodes = [node]
        stack = [node]
        currentIndex = 1
        while len(stack) > 0:
            tmpNode = stack.pop()
            for i in tmpNode.neighbors:
                if not (i in nodes):
                    nodes.append(i)
                    stack.append(i)
                    node2Index[i] = currentIndex
                    currentIndex += 1
        res = []
        for i in range(currentIndex):
            res.append(Node(nodes[i].val, []))
        for i in range(currentIndex):
            res[i].neighbors = []
            for j in nodes[i].neighbors:
                res[i].neighbors.append(res[node2Index[j]])
        return res[0]
