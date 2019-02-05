class Solution:
    def sortColors(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        r, w, b = 0, 0, len(nums) - 1
        while w <= b:
            if nums[w] == 0:
                tmp = nums[w]
                nums[w] = nums[r]
                nums[r] = tmp
                w += 1
                r += 1
            elif nums[w] == 1:
                w += 1
            else:
                tmp = nums[w]
                nums[w] = nums[b]
                nums[b] = tmp
                b -= 1
