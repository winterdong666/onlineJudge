class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binarySearch(nums, l, r, target):
            if l > r:
                return -1
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                return binarySearch(nums, l, m - 1, target)
            else:
                return binarySearch(nums, m + 1, r, target)
        for i in range(len(numbers)):
            m = binarySearch(numbers, i + 1, len(numbers) - 1, target - numbers[i])
            if m != -1:
                return [i + 1, m + 1]
        return [-1, -1]
