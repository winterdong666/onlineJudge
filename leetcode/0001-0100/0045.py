class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        l = 0
        r = nums[0]
        count = 1
        while r < len(nums) - 1:
            count += 1
            nextMax = 0
            for i in range(l, r + 1):
                nextMax = max(nextMax, i + nums[i])
            l = r + 1
            r = nextMax
        return count
