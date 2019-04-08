class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        bricks = {}
        for i in wall:
            t = 0
            for j in range(len(i) - 1):
                t = t + i[j]
                bricks[t] = bricks.get(t, 0) + 1
        res = 0
        for i in bricks.keys():
            res = max(res, bricks[i])
        return len(wall) - res
