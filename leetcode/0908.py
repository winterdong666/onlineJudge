class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        A.sort()
        if len(A) <= 1:
            return 0
        if A[-1] - A[0] <= 2 * K:
            return 0
        else:
            return A[-1] - A[0] - 2 * K
