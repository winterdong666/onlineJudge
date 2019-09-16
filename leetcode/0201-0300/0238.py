class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        tmp = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            res[i] = res[i + 1] * nums[i + 1]
        for i in range(1, len(nums)):
            tmp[i] = tmp[i - 1] * nums[i - 1]
        for i in range(len(nums)):
            res[i] *= tmp[i]
        return res
