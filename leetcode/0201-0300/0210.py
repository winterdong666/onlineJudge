class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0:
            return []
        elif numCourses == 1:
            return [0]
        direction = []
        for i in range(numCourses):
            direction.append([])
        numOfPre = [0] * numCourses
        for i in prerequisites:
            out = i[1]
            into = i[0]
            numOfPre[into] += 1
            direction[out].append(into)
        res = []
        topo = []
        for i in range(numCourses):
            if numOfPre[i] == 0:
                topo.append(i)
        while len(topo) > 0:
            t = topo.pop()
            res.append(t)
            for i in direction[t]:
                numOfPre[i] -= 1
                if numOfPre[i] == 0:
                    topo.append(i)
        if len(res) < numCourses:
            return []
        else:
            return res
