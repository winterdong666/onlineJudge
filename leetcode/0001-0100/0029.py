class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if abs(dividend) < abs(divisor):
            return 0
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        sign = True
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = False
        
        up = abs(dividend)
        down = abs(divisor)
        res = 0
        while up >= down:
            tmp = down
            r = 1
            while tmp <= up:
                tmp <<= 1
                r <<= 1
            tmp >>= 1
            r >>= 1
            up -= tmp
            res += r
        
        if sign:
            return res
        else:
            return -res
