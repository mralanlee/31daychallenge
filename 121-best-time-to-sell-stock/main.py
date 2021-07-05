class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice, profit = prices[0], 0

        for price in prices:
            if price < minPrice:
                minPrice = price

            curr = price - minPrice
            if curr > profit:
                profit = curr

        return profit
