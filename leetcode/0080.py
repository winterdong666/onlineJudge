class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        if len(nums) <= 1:
            return len(nums)
        p = 1
        count = 1
        c = 1
        while c < len(nums):
            if nums[c] == nums[c - 1]:
                count += 1
                if count <= 2:
                    nums[p] = nums[c]
                    p += 1
            else:
                count = 1
                nums[p] = nums[c]
                p += 1
            c += 1
        while len(nums) > p:
            nums.pop()
        return len(nums)
