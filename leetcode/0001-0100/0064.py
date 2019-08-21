class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == [] or grid[0] == []:
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0:
                    if j > 0:
                        grid[i][j] = grid[i][j - 1] + grid[i][j]
                else:
                    if j == 0:
                        grid[i][j] = grid[i - 1][j] + grid[i][j]
                    else:
                        grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]
