class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
            if dic[i] >= 2:
                return True
        return False
