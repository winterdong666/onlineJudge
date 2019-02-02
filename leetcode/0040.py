class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        tmpC = candidates[:]
        while len(tmpC) > 0 and tmpC[-1] > target:
            tmpC.pop()
        if len(tmpC) == 0:
            if target == 0:
                return [[]]
            else:
                return []
        
        res1 = self.combinationSum2(candidates[:-1], target - candidates[-1])
        for i in range(len(res1)):
            res1[i].append(candidates[-1])
        
        res2 = self.combinationSum2(candidates[:-1], target)
        for i in res2:
            if not (i in res1):
                res1.append(i)
        
        return res1
