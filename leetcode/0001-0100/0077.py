class Solution:
    def combine(self, n: 'int', k: 'int') -> 'List[List[int]]':
        def combineHelper(n, start, k):
            res = []
            if k == 1:
                for i in range(start, n + 1):
                    res.append([i])
                return res
            else:
                for i in range(start, n - k + 2):
                    tmp = combineHelper(n, i + 1, k - 1)
                    for j in tmp:
                        j.append(i)
                        res.append(j)
                return res
        return combineHelper(n, 1, k)
