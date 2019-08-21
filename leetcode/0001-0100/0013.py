class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        tranverse = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = tranverse[s[-1]]
        for i in range(len(s) - 1):
            if tranverse[s[i]] < tranverse[s[i + 1]]:
                res -= tranverse[s[i]]
            else:
                res += tranverse[s[i]]
        return res
