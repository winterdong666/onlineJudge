class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        p = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            else:
                nums[p] = nums[i]
                p += 1
        while len(nums) > p:
            nums.pop()
        return p
