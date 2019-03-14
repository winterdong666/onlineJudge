class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k >= len(nums):
            k -= len(nums)
        if k == 0:
            return
        tmp = []
        for i in range(len(nums) - k, len(nums)):
            tmp.append(nums[i])
        for i in range(len(nums) - 1, k - 1, -1):
            nums[i] = nums[i - k]
        for i in range(k):
            nums[i] = tmp[i]
