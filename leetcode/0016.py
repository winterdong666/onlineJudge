class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = 2147483647
        resSum = 0
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r] - target
                if s < 0:
                    if (-s) < res:
                        res = (-s)
                        resSum = s + target
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif s == 0:
                    return target
                else:
                    if s < res:
                        res = s
                        resSum = s + target
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return resSum
