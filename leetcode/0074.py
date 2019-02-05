class Solution:
    def searchMatrix(self, matrix: 'List[List[int]]', target: 'int') -> 'bool':
        if matrix == [] or matrix[0] == []:
            return False
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] == target:
                return True
            elif matrix[m][0] < target:
                l = m + 1
            else:
                r = m - 1
        if l >= len(matrix):
            l -= 1
        if matrix[l][0] == target:
            return True
        if matrix[l][0] > target:
            while matrix[l][0] > target:
                l -= 1
                if l < 0:
                    l += 1
                    break
                if matrix[l][0] == target:
                    return True
        else:
            while matrix[l][0] < target and l < len(matrix):
                l += 1
                if l >= len(matrix):
                    break
                if matrix[l][0] == target:
                    return True
            l -= 1
        l1, r1 = 0, len(matrix[0]) - 1
        while l1 <= r1:
            m1 = (l1 + r1) // 2
            if matrix[l][m1] == target:
                return True
            elif matrix[l][m1] < target:
                l1 = m1 + 1
            else:
                r1 = m1 - 1
        return False
