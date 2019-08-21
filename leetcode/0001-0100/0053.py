class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        current = nums[0]
        if current < 0:
            current = 0
        for i in range(1, len(nums)):
            current += nums[i]
            res = max(res, current)
            if current < 0:
                current = 0
        return res
