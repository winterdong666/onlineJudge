class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        last = True
        t = len(nums) - 1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                last = False
                t = i - 1
                break
        if last:
            for i in range(len(nums) // 2):
                tmp = nums[i]
                nums[i] = nums[len(nums) - 1 - i]
                nums[len(nums) - 1 - i] = tmp
        else:
            l = len(nums) - 1
            for i in range(len(nums) - 1, t, -1):
                if nums[i] > nums[t]:
                    l = i
                    break
            tmp = nums[t]
            nums[t] = nums[l]
            nums[l] = tmp
            for i in range((len(nums) - t) // 2):
                tmp = nums[t + 1 + i]
                nums[t + 1 + i] = nums[len(nums) - 1 - i]
                nums[len(nums) - 1 - i] = tmp
