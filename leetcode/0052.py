class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        def DFS(index, dif, sums, n):
            count = 0
            c = len(index)
            if c >= n:
                return 1
            for l in range(n):
                if (l not in index) and (c - l not in dif) and (c + l not in sums): 
                    count += DFS(index + [l], dif + [c - l], sums + [c + l], n)
            return count
        return DFS([], [], [], n)
