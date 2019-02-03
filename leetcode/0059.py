class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def generateMatrixHelper(matrix, start, index, n):
            if n <= 0:
                return
            if n == 1:
                matrix[index][index] = start
                return
            x, y = index, index
            for i in range(n - 1):
                matrix[x][y] = start
                start += 1
                y += 1
            for i in range(n - 1):
                matrix[x][y] = start
                start += 1
                x += 1
            for i in range(n - 1):
                matrix[x][y] = start
                start += 1
                y -= 1
            for i in range(n - 1):
                matrix[x][y] = start
                start += 1
                x -= 1
            generateMatrixHelper(matrix, start, index + 1, n - 2)
        if n == 0:
            return [[]]
        matrix = []
        for i in range(n):
            tmp = []
            for j in range(n):
                tmp.append(0)
            matrix.append(tmp)
        generateMatrixHelper(matrix, 1, 0, n)
        return matrix
