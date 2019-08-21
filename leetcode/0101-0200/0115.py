class Solution:
    def numDistinct(self, s: 'str', t: 'str') -> 'int':
        l1, l2 = len(s), len(t)
        DP = []
        for i in range(l1 + 1):
            tmp = []
            tmp.append(1)
            for j in range(l2):
                tmp.append(0)
            DP.append(tmp)
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if i == j:
                    if s[:i] == t[:j]:
                        DP[i][j] = 1
                    else:
                        DP[i][j] = 0
                elif i > j:
                    if s[i - 1] == t[j - 1]:
                        DP[i][j] = DP[i - 1][j] + DP[i - 1][j - 1]
                    else:
                        DP[i][j] = DP[i - 1][j]
        return DP[-1][-1]
