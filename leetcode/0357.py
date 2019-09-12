class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        DP = [1, 10]
        for i in range(2, 11):
            res = 9
            for j in range(9, 10 - i, -1):
                res *= j
            DP.append(DP[-1] + res)
        if n >= 11:
            return DP[-1]
        else:
            return DP[n]
