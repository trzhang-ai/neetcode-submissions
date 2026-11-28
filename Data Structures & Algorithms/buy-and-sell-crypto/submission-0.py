class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            buy = prices[i]
            sell = max(prices[i + 1:])
            profit = sell - buy
            max_profit = max(max_profit, profit)
        return max_profit