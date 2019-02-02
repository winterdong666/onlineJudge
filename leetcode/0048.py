class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        def rotateLayer(matrix, l, r):
            if l >= r:
                return
            for i in range(r - l):
                tmp = matrix[l][l + i]
                matrix[l][l + i] = matrix[r - i][l]
                matrix[r - i][l] = matrix[r][r - i]
                matrix[r][r - i] = matrix[l + i][r]
                matrix[l + i][r] = tmp
            rotateLayer(matrix, l + 1, r - 1)
        rotateLayer(matrix, 0, len(matrix) - 1)
