class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        DP = []
        res = 0
        for i in range(m + 1):
            tmp = []
            for j in range(n + 1):
                if i == 0 or j == 0 or matrix[i - 1][j - 1] == "0":
                    tmp.append(0)
                else:
                    tmp.append(1)
            DP.append(tmp)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == "1":
                    DP[i][j] = min(DP[i - 1][j - 1], DP[i - 1][j], DP[i][j - 1]) + 1
                    if DP[i][j] > res:
                        res = DP[i][j]
        return res * res
