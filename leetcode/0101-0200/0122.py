class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        if len(prices) == 0:
            return 0
        profit = 0
        current = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < prices[i - 1]:
                profit += (prices[i - 1] - current)
                current = prices[i]
        profit += (prices[-1] - current)
        return profit
