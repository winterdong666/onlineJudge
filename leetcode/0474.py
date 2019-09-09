class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def counts(s):
            zeros, ones = 0, 0
            for i in s:
                if i == "0":
                    zeros += 1
                else:
                    ones += 1
            return zeros, ones
        
        DP = []
        for i in range(m + 1):
            tmp = []
            for j in range(n + 1):
                tmp.append(0)
            DP.append(tmp)
        for s in strs:
            zeros, ones = counts(s)
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    DP[i][j] = max(DP[i][j], 1 + DP[i - zeros][j - ones])
        return DP[-1][-1]
