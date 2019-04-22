'''
Idea from @heiyanbin
Use a DP matrix to optimize the Palindrome Judgement
'''

class Solution:
    def minCut(self, s: str) -> int:
        pal = []
        lens = len(s)
        for i in range(lens):
            t = []
            for j in range(lens):
                t.append(False)
            pal.append(t)
        DP = [2147483647] * lens
        for i in range(lens - 1, -1, -1):
            for j in range(lens - 1, i - 1, -1):
                if s[i] == s[j] and (j - i < 2 or pal[i + 1][j - 1]):
                    pal[i][j] = True
                    if j == lens - 1:
                        DP[i] = 0
                    else:
                        DP[i] = min(DP[i], 1 + DP[j + 1])
        return DP[0]
