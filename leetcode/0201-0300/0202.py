class Solution:
    def isHappy(self, n: int) -> bool:
        used = []
        while n != 1:
            tmp = 0
            while n != 0:
                t = n % 10
                tmp += t * t
                n //= 10
            if tmp in used:
                return False
            n = tmp
            used.append(n)
        return True
