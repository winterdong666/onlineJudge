class Solution:
    def bestRotation(self, A: List[int]) -> int:
        def findRange(n, i, iniIndex):
            if i >= n:
                return []
            if iniIndex < i:
                return [[iniIndex + 1, iniIndex + n - i]]
            else:
                return [[0, iniIndex - i], [iniIndex + 1, n - 1]]
        
        res, resIndex = 0, 0
        n = len(A)
        ans = [0] * n
        for i in range(n):
            tmp = findRange(n, A[i], i)
            for j in tmp:
                if j[0] > j[1]:
                    continue
                ans[j[0]] += 1
                if j[1] + 1 < n:
                    ans[j[1] + 1] -= 1
        count = 0
        for i in range(n):
            count += ans[i]
            if count > res:
                res = count
                resIndex = i
        return resIndex
