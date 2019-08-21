class Solution:
    def numTrees(self, n: 'int') -> 'int':
        DP = []
        if n <= 1:
            return 1
        DP.append(1)
        DP.append(1)
        for i in range(2, n + 1):
            tmp = 0
            for j in range(0, i):
                tmp += DP[j] * DP[- j - 1]
            DP.append(tmp)
        return DP[-1]
