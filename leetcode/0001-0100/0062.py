class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        DP = []
        for i in range(n):
            tmp = []
            for j in range(m):
                if i == 0:
                    tmp.append(1)
                else:
                    if j == 0:
                        tmp.append(1)
                    else:
                        tmp.append(tmp[-1] + DP[i - 1][j])
            DP.append(tmp)
        return DP[-1][-1]
