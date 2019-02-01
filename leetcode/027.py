class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums == []:
            return 0
        
        p = 0
        for i in range(len(nums)):
            if val != nums[i]:
                nums[p] = nums[i]
                p += 1
        
        while len(nums) > p:
            nums.pop()
        
        return p
