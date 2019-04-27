class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def recursion(nums, l, r):
            if r <= 0:
                return 0
            if l >= len(nums) - 1:
                return len(nums) - 1
            if l == r:
                return l
            if l == r - 1:
                if nums[l] > nums[r]:
                    return l
                else:
                    return r
            m = l + (r - l) // 2
            if nums[m] > nums[m - 1] and nums[m] > nums[m + 1]:
                return m
            elif nums[m] < nums[m - 1]:
                return recursion(nums, l, m - 1)
            else:
                return recursion(nums, m + 1, r)
        return recursion(nums, 0, len(nums) - 1)
