class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        if i < 0:
            return 0
        c = 0
        while i >= 0 and s[i] != ' ':
            i -= 1
            c += 1
        return c
