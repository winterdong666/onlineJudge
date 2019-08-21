class Solution:
    def subsets(self, nums: 'List[int]') -> 'List[List[int]]':
        def subsetsHelper(nums, pointer):
            if pointer >= len(nums):
                return [[]]
            tmp = subsetsHelper(nums, pointer + 1)
            res = []
            for i in tmp:
                res.append(i[:])
                i.append(nums[pointer])
                res.append(i[:])
            return res
        return subsetsHelper(nums, 0)
