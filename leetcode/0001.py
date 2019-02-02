class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        for i in range(l):
            tmp = target - nums[i]
            for j in range(i + 1, l):
                if nums[j] == tmp:
                    res = [i, j]
                    return res
