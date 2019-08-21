class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k > len(nums):
            k -= len(nums)
        if k == 0:
            return
        l = len(nums) - k
        for i in range(l // 2):
            tmp = nums[i]
            nums[i] = nums[l - 1 - i]
            nums[l - 1 - i] = tmp
        for i in range(k // 2):
            tmp = nums[l + i]
            nums[l + i] = nums[-1 - i]
            nums[-1 - i] = tmp
        for i in range(len(nums) // 2):
            tmp = nums[i]
            nums[i] = nums[-1 - i]
            nums[-1 - i] = tmp
