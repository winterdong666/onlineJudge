class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = 0
        for i in range(len(nums) - 1):
            res = max(res, nums[i + 1] - nums[i])
        return res
