class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        buy1, sell1, buy2, sell2 = -2147483647, 0, -2147483647, 0
        for i in prices:
            buy1 = max(buy1, -i)
            sell1 = max(sell1, buy1 + i)
            buy2 = max(buy2, sell1 - i)
            sell2 = max(sell2, buy2 + i)
        return sell2
