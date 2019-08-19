class Solution:
    def findMin(self, nums: List[int]) -> int:
        def helper(nums, l, r):
            if l == r:
                return nums[l]
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                return helper(nums, m + 1, r)
            else:
                return helper(nums, l, m)
        return helper(nums, 0, len(nums) - 1)
