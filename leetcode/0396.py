class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        s = 0
        tmpRes = 0
        res = 0
        l = len(A)
        for i in range(l):
            s += A[i]
            tmpRes += A[i] * i
        res = tmpRes
        for i in range(l - 1, 0, -1):
            tmpRes = tmpRes + s - l * A[i]
            res = max(res, tmpRes)
        return res
