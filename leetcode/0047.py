class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        res = []
        dic = {}
        for i in range(len(nums)):
            if dic.get(nums[i], 0) == 0:
                tmp = nums[0]
                nums[0] = nums[i]
                nums[i] = tmp
                tmpRes = self.permuteUnique(nums[1:])
                for j in tmpRes:
                    j.append(nums[0])
                    res.append(j)
                tmp = nums[0]
                nums[0] = nums[i]
                nums[i] = tmp
                dic[nums[i]] = 1
        return res
