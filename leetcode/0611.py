class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        first = 0
        l = len(nums)
        res = 0
        while first < l - 2:
            last = first + 2
            for second in range(first + 1, l - 1):
                if last <= second:
                    last = second + 1
                while last < l and nums[first] + nums[second] > nums[last]:
                    last += 1
                res += (last - second - 1)
            first += 1
        return res
