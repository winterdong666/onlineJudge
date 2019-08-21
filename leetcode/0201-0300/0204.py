class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        count = 0
        table = [0] * (n - 1)
        table[0] = 1
        for i in range(1, n - 1):
            if table[i] == 0:
                count += 1
                for j in range(2 * i + 1, n - 1, i + 1):
                    table[j] = 1
        return count
