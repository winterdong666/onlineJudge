class Solution:
    def mySqrt(self, x: 'int') -> 'int':
        if x == 0 or x == 1:
            return x
        l, r = 0, x
        while l < r:
            m = (l + r) // 2
            if m * m == x:
                return m
            elif m * m > x:
                r = m - 1
            else:
                l = m + 1
        if l * l == x:
            return l
        else:
            while l * l < x:
                l += 1
                if l * l == x:
                    return l
                elif l * l > x:
                    return l - 1
            while l * l > x:
                l -= 1
                if l * l <= x:
                    return l
