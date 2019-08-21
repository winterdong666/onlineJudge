class Solution:
    def rob(self, nums: List[int]) -> int:
        res = []
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        res.append(nums[0])
        res.append(max(nums[0], nums[1]))
        for i in range(2, len(nums)):
            res.append(max(res[i - 2] + nums[i], res[i - 1]))
        return res[-1]
