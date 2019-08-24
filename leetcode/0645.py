class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        error = 0
        total = 0
        l = len(nums)
        c = [0] * l
        for i in nums:
            c[i - 1] += 1
            if c[i - 1] == 2:
                error = i
            total += i
        diff = total - (1 + l) * l // 2
        return [error, error - diff]
