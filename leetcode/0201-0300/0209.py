class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        for i in nums:
            if i >= s:
                return 1
        if nums == []:
            return 0
        head, tail, total, res = 0, 0, nums[0], 2147483647
        #show = ()
        while tail < len(nums) - 1:
            tail += 1
            total += nums[tail]
            if total >= s:
                while total >= s:
                    total -= nums[head]
                    head += 1
                head -= 1
                total += nums[head]
                if tail - head + 1 < res:
                    res = tail - head + 1
                    #show = (head, tail)
        if res == 2147483647:
            return 0
        else:
            return res
