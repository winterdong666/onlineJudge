class Solution:
    def addDigits(self, num: int) -> int:
        res = 0
        while num != 0:
            res += num % 10
            if res >= 10:
                res = res % 10 + 1
            num //= 10
        return res
