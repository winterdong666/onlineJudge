class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 1:
            return "1"
        count = 1
        for i in range(n - 1):
            count = count * (i + 1)
        digit = []
        for i in range(n):
            digit.append(str(i + 1))
        def getPermutationHelper(k, n, count, digit):
            if n == 1:
                return digit[0]
            if k == 0:
                tmpStr = digit[-1]
                digit1 = digit[:-1]
            else:
                tmp = (k - 1) // count
                tmpStr = digit[tmp]
                digit1 = digit[:tmp] + digit[tmp + 1:]
            return tmpStr + getPermutationHelper(k % count, n - 1, count // (n - 1), digit1)
        return getPermutationHelper(k, n, count, digit)
