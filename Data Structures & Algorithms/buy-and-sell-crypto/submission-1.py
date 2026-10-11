class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = float("inf")
        for price in prices:
            if price < buy:
                buy = price
            profit = max(profit, price - buy)
        
        return profit