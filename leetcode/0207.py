class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses <= 1:
            return True
        direction = []
        for i in range(numCourses):
            direction.append([])
        numOfPre = [0] * numCourses
        for i in prerequisites:
            out = i[1]
            into = i[0]
            numOfPre[into] += 1
            direction[out].append(into)
        count = 0
        topo = []
        for i in range(numCourses):
            if numOfPre[i] == 0:
                topo.append(i)
        while len(topo) > 0:
            t = topo.pop()
            count += 1
            for i in direction[t]:
                numOfPre[i] -= 1
                if numOfPre[i] == 0:
                    topo.append(i)
        if count == numCourses:
            return True
        else:
            return False
