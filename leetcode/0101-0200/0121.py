class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        mini = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > mini:
                profit = max(profit, prices[i] - mini)
            else:
                mini = prices[i]
        return profit
