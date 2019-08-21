class Solution:
    def numDecodings(self, s: 'str') -> 'int':
        if s == "":
            return 0
        if s[0] == '0':
            return 0
        if len(s) == 1:
            if int(s) == 0:
                return 0
            return 1
        DP = [1, 1]
        for i in range(1, len(s)):
            if int(s[i - 1: i + 1]) == 0:
                return 0
            if int(s[i]) == 0:
                if int(s[i - 1]) > 2:
                    return 0
                DP.append(DP[i - 1])
            elif int(s[i - 1: i + 1]) <= 26 and s[i - 1] != '0':
                DP.append(DP[i - 1] + DP[i])
            else:
                DP.append(DP[i])
        return DP[-1]
