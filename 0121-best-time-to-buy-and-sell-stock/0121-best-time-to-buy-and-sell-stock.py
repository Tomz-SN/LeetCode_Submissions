class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        minimum = prices[0]
        for price in prices:
            minimum = min(minimum,price)
            profit = max(profit, price - minimum)
        return profit