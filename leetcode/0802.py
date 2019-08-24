class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        inGraph = []
        for i in range(len(graph)):
            inGraph.append([])
        countOut = [0] * len(graph)
        for i in range(len(graph)):
            countOut[i] = len(graph[i])
            for j in graph[i]:
                inGraph[j].append(i)
        DFS = []
        for i in range(len(graph)):
            if countOut[i] == 0:
                DFS.append(i)
        while len(DFS) > 0:
            t = DFS.pop()
            for i in inGraph[t]:
                countOut[i] -= 1
                if countOut[i] == 0:
                    DFS.append(i)
        res = []
        for i in range(len(countOut)):
            if countOut[i] == 0:
                res.append(i)
        return res
        
