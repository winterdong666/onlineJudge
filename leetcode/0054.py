class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        def recursive(matrix, l, r, u, d, res):
            if l > r or u > d:
                return
            if l == r:
                for i in range(u, d + 1):
                    res.append(matrix[i][l])
                return
            if u == d:
                for i in range(l, r + 1):
                    res.append(matrix[u][i])
                return
            x, y = l, u
            while x < r:
                res.append(matrix[y][x])
                x += 1
            while y < d:
                res.append(matrix[y][x])
                y += 1
            while x > l:
                res.append(matrix[y][x])
                x -= 1
            while y > u:
                res.append(matrix[y][x])
                y -= 1
            recursive(matrix, l + 1, r - 1, u + 1, d - 1, res)
        if matrix == []:
            return []
        if matrix == [[]]:
            return []
        l, r, u, d = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        res = []
        recursive(matrix, l, r, u, d, res)
        return res
