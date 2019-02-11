class Solution:
    def isInterleave(self, s1: 'str', s2: 'str', s3: 'str') -> 'bool':
        if len(s1) + len(s2) != len(s3):
            return False
        l1 = len(s1)
        l2 = len(s2)
        DP = []
        for i in range(l1 + 1):
            DP.append([False] * (l2 + 1))
        DP[0][0] = True
        for i in range(l2):
            DP[0][i + 1] = DP[0][i] and (s2[i] == s3[i])
        for i in range(l1):
            DP[i + 1][0] = DP[i][0] and (s1[i] == s3[i])
        for i in range(l1):
            for j in range(l2):
                DP[i + 1][j + 1] = (s2[j] == s3[i + j + 1] and DP[i + 1][j]) or (s1[i] == s3[i + j + 1] and DP[i][j + 1])
        return DP[-1][-1]
