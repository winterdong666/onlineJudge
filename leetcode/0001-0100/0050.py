class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        pos = True
        if n < 0:
            pos = False
            n = -n
        
        twoBase = []
        while n != 0:
            twoBase.append(n % 2)
            n //= 2
        res = 1
        base = x
        for i in range(len(twoBase)):
            if twoBase[i] == 1:
                res = res * base
            base = base * base
        if pos == False:
            res = 1 / res
        return res
