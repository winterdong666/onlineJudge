class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        tmp = candidates[:]
        res = [[]]
        while len(tmp) > 0 and tmp[-1] > target:
            tmp.pop()
        if len(tmp) == 0:
            if target > 0:
                return []
            else:
                return res
        res1 = self.combinationSum(tmp, target - tmp[-1])
        for i in range(len(res1)):
            res1[i].append(tmp[-1])
        res2 = self.combinationSum(tmp[:-1], target)
        
        return res1 + res2
