class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        p = self.countAndSay(n - 1)
        res = ""
        t = p[0]
        count = 1
        for i in range(1, len(p)):
            if p[i] == p[i - 1]:
                count += 1
            else:
                res = res + str(count)
                res = res + t
                t = p[i]
                count = 1
        res = res + str(count)
        res = res + t
        return res
