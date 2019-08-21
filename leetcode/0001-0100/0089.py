class Solution:
    def grayCode(self, n: 'int') -> 'List[int]':
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        res = self.grayCode(n - 1)
        base = 1
        for i in range(n - 1):
            base *= 2
        for i in range(len(res) - 1, -1, -1):
            res.append(res[i] + base)
        return res
