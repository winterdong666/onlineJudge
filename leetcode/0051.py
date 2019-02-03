class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def DFS(resIndex, index, dif, sums, n):
            c = len(index)
            if c >= n:
                resIndex.append(index)
                return
            for l in range(n):
                if (l not in index) and (c - l not in dif) and (c + l not in sums): 
                    DFS(resIndex, index + [l], dif + [c - l], sums + [c + l], n)  
        resIndex = []
        DFS(resIndex ,[], [], [], n)
        res = []
        for i in resIndex:
            tmp = []
            for j in i:
                tmp.append("." * j + "Q" + "." * (n - j - 1))
            res.append(tmp)
        return res
