class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return ""
        res = s[0]
        resL = 1
        for i in range(1, len(s)):
            tmpL = 1
            for j in range(1, min(i + 1, len(s) - i)):
                if s[i - j] == s[i + j]:
                    tmpL += 2
                    if tmpL > resL:
                        resL = tmpL
                        res = s[i - j: i + j + 1]
                else:
                    break
        for i in range(0, len(s) - 1):
            if s[i] == s[i + 1]:
                tmpL = 2
                if tmpL > resL:
                    resL = tmpL
                    res = s[i: i + 2]
                for j in range(1, min(i + 1, len(s) - i - 1)):
                    if s[i - j] == s[i + 1 + j]:
                        tmpL += 2
                        if tmpL > resL:
                            resL = tmpL
                            res = s[i - j: i + j + 2]
                    else:
                        break
        return res
