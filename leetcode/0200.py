class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        h, w = len(grid), len(grid[0])
        for i in range(h):
            for j in range(w):
                if grid[i][j] == "1":
                    count += 1
                    DFS = [(i, j)]
                    while len(DFS) > 0:
                        x, y = DFS.pop()
                        if grid[x][y] == "0":
                            continue
                        grid[x][y] = "0"
                        if x > 0 and grid[x - 1][y] == "1":
                            DFS.append((x - 1, y))
                        if y > 0 and grid[x][y - 1] == "1":
                            DFS.append((x, y - 1))
                        if x < h - 1 and grid[x + 1][y] == "1":
                            DFS.append((x + 1, y))
                        if y < w - 1 and grid[x][y + 1] == "1":
                            DFS.append((x, y + 1))
        return count
