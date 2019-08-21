class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        res = 0
        for i in nums:
            if dic.get(i - 1, 0) == 0:
                j = i + 1
                while dic.get(j, 0) != 0:
                    j += 1
                res = max(res, j - i)
        return res
