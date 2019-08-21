class Solution:
    def findMin(self, nums: List[int]) -> int:
        def helper(nums, l, r):
            if l == r:
                return nums[l]
            if l == r - 1:
                return min(nums[l], nums[r])
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                return helper(nums, m + 1, r)
            elif nums[m] == nums[r]:
                return min(helper(nums, l, m), helper(nums, m, r))
            else:
                return helper(nums, l, m)
        return helper(nums, 0, len(nums) - 1)
