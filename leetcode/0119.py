class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        res = [1]
        base = 1
        for i in range(rowIndex):
            base = base * (rowIndex - i) // (i + 1)
            res.append(base)
        return res
