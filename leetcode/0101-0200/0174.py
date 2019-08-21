class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        DP = []
        m = len(dungeon)
        n = len(dungeon[0])
        for i in range(m):
            DP.append([0] * n)
        for i in range(m)[::-1]:
            for j in range(n)[::-1]:
                if i == m - 1:
                    if j == n - 1:
                        DP[i][j] = max(1 - dungeon[i][j], 1)
                    else:
                        DP[i][j] = max(DP[i][j + 1] - dungeon[i][j], 1)
                else:
                    if j == n - 1:
                        DP[i][j] = max(DP[i + 1][j] - dungeon[i][j], 1)
                    else:
                        DP[i][j] = max(min(DP[i + 1][j], DP[i][j + 1]) - dungeon[i][j], 1)
        return DP[0][0]
