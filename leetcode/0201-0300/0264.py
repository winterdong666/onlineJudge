from queue import PriorityQueue

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        q = PriorityQueue()
        used = {1: 1}
        q.put(1)
        cur = 0
        for i in range(n):
            cur = q.get()
            if used.get(cur * 2, 0) == 0:
                q.put(cur * 2)
                used[cur * 2] = 1
            if used.get(cur * 3, 0) == 0:
                q.put(cur * 3)
                used[cur * 3] = 1
            if used.get(cur * 5, 0) == 0:
                q.put(cur * 5)
                used[cur * 5] = 1
        return cur
