class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = -2147483647
        count = 0
        for i in range(k):
            count += nums[i]
        if count > res:
            res = count
        for i in range(k, len(nums)):
            count += nums[i]
            count -= nums[i - k]
            if count > res:
                res = count
        return res / k
