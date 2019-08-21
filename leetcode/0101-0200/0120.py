class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        res = []
        resMin = 2147483647
        for i in range(len(triangle)):
            tmp = []
            for j in range(len(triangle[i])):
                if i == 0:
                    tmp.append(triangle[0][0])
                elif j == 0:
                    tmp.append(res[i - 1][0] + triangle[i][0])
                elif j == len(triangle[i]) - 1:
                    tmp.append(res[i - 1][i - 1] + triangle[i][-1])
                else:
                    tmp.append(min(res[i - 1][j - 1], res[i - 1][j]) + triangle[i][j])
                if i == len(triangle) - 1:
                    resMin = min(resMin, tmp[-1])
            res.append(tmp)
        return resMin
