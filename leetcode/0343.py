class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        maxi = [0] * (n + 1)
        maxi[1] = 1
        maxi[2] = 2
        for i in range(3, n + 1):
            tmp = 0
            for j in range(1, i // 2 + 1):
                tmp = max(tmp, maxi[j] * maxi[i - j])
            if i == n:
                return tmp
            maxi[i] = max(tmp, i)
