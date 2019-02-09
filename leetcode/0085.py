class Solution:
    def maximalRectangle(self, matrix: 'List[List[str]]') -> 'int':
        if not matrix:
            return 0
        h, w = len(matrix), len(matrix[0])
        m = []
        for i in range(h):
            tmp = []
            for j in range(w):
                tmp.append(0)
            m.append(tmp)
        for j in range(h):
            for i in range(w):
                if matrix[j][i] == '1':
                    m[j][i] = m[j-1][i] + 1
        res = 0
        for row in m:
            res = max(res, self.findLargestRectangle(row))
        return res
    
    def findLargestRectangle(self, row):
        height = 0
        row.append(0)
        stack = [-1]
        for i in range(len(row)):
            while row[i] < row[stack[-1]]:
                h = row[stack.pop()]
                w = i - stack[-1] - 1
                height = max(height, h * w)
            stack.append(i)
        return height
