class Solution:
    def binaryGap(self, N: int) -> int:
        count = 0
        res = 0
        first = True
        while N != 0:
            if N % 2 == 0:
                if first:
                    N //= 2
                    continue
                else:
                    count += 1
            else:
                if first:
                    first = False
                else:
                    res = max(res, count + 1)
                    count = 0
            N //= 2
        return res
