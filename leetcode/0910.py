class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        if len(A) <= 1:
            return 0
        if len(A) == 2:
            return min(A[1] - A[0], abs(A[1] - (A[0] + 2 * K)))
        res = A[-1] - A[0]
        for i in range(len(A) - 1):
            A[i] += 2 * K
            res = min(res, max(A[i], A[-1]) - min(A[i + 1], A[0]))
        return res
