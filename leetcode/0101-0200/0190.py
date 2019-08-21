class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        tmp = []
        while n > 0:
            tmp.append(n % 2)
            n = n // 2
        while len(tmp) < 32:
            tmp.append(0)
        base = 1
        res = 0
        for i in range(len(tmp) - 1, -1, -1):
            res = res + tmp[i] * base
            base <<= 1
        return res
