class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        res = []
        for i in range(len(nums)):
                tmp = nums[0]
                nums[0] = nums[i]
                nums[i] = tmp
                tmpRes = self.permute(nums[1:])
                for j in tmpRes:
                    j.append(nums[0])
                    res.append(j)
                tmp = nums[0]
                nums[0] = nums[i]
                nums[i] = tmp
        return res
