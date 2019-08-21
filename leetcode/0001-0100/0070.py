class Solution:
    def climbStairs(self, n: 'int') -> 'int':
        if n <= 1:
            return 1
        DP = [1, 1]
        for i in range(2, n + 1):
            DP.append(DP[-1] + DP[-2])
        return DP[-1]
