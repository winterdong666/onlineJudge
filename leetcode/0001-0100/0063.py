class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid == [] or obstacleGrid[0] == []:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0
        DP = []
        for i in range(len(obstacleGrid)):
            tmp = []
            for j in range(len(obstacleGrid[0])):
                if i == 0:
                    if j == 0:
                        tmp.append(1)
                    elif obstacleGrid[i][j] == 0:
                        tmp.append(tmp[-1])
                    else:
                        tmp.append(0)
                else:
                    if obstacleGrid[i][j] == 1:
                        tmp.append(0)
                    elif j == 0:
                        tmp.append(DP[i - 1][0])
                    else:
                        tmp.append(DP[i - 1][j] + tmp[-1])
            DP.append(tmp)
        return DP[-1][-1]
