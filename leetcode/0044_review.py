class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ls = len(s)
        lp = len(p)
        #When substring of p is zero only when s is zero the result is True
        DP = [True] + [False] * ls
        for i in range(lp):
            if p[i] != '*':
                for j in range(ls - 1, -1, -1):
                    #When p[i] is not *, then relies on (i-1,j-1) and p[i] == s[j]
                    DP[j + 1] = DP[j] and (p[i] == s[j] or p[i] == '?')
                DP[0] = False
            else:
                for j in range(1, ls + 1):
                    #When p[i] is *, then relies on (i, j - 1)('*' represents at least s[j]) or (i - 1, j)('*' represents nothing)
                    DP[j] = DP[j - 1] or DP[j]
        return DP[-1]
