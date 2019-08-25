class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        DP = []
        l1, l2 = len(word1), len(word2)
        for i in range(l1 + 1):
            t = [0] * (l2 + 1)
            DP.append(t)
        
        for i in range(l1 + 1):
            for j in range(l2 + 1):
                if i == 0:
                    DP[i][j] = j
                elif j == 0:
                    DP[i][j] = i
                else:
                    if word1[i - 1] == word2[j - 1]:
                        DP[i][j] = DP[i - 1][j - 1]
                    else:
                        DP[i][j] = min(DP[i - 1][j], DP[i][j - 1]) + 1
        return DP[-1][-1]
