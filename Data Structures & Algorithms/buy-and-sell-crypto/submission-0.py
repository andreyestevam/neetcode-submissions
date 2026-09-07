class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price_so_far = prices[0]
        for i in range(len(prices)):
            if prices[i] < min_price_so_far:
                min_price_so_far = prices[i]
            profit = prices[i] - min_price_so_far
            if profit > max_profit:
                max_profit = profit
        return max_profit