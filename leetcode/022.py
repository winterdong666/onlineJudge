class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def recursive(l, r):
            res = []
            if l == 0 and r == 0:
                return res
            if l == 0 and r == 1:
                res.append(")")
                return res
            tmp1 = []
            tmp2 = []
            if l > 0:
                tmp1 = recursive(l - 1, r)
            if r > l:
                tmp2 = recursive(l, r - 1)
            for i in tmp1:
                res.append('(' + i)
            for i in tmp2:
                res.append(')' + i)
            return res
        return recursive(n, n)
