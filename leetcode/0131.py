class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if s == "":
            return []
        if len(s) == 1:
            return [[s]]
        pal = []
        lens = len(s)
        DP = []
        for i in range(len(s)):
            tmpPal = []
            for j in range(len(s)):
                tmpPal.append(False)
            pal.append(tmpPal)
            DP.append([])
        DP[0] = [[s[0]]]
        pal[0][0] = True
        for j in range(1, lens):
            for i in range(0, j + 1):
                if s[i] == s[j] and (j - i < 2 or pal[i + 1][j - 1]):
                    pal[i][j] = True
                    if i == 0:
                        DP[j].append([s[i: j + 1]])
                    else:
                        for l in DP[i - 1]:
                            t = l[:]
                            t.append(s[i: j + 1])
                            DP[j].append(t)
        return DP[-1]
