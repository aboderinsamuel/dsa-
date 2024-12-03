from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        min_price = float('inf')  # Initialize to a very high value
        max_profit = 0

        for price in prices:
        # Update the minimum price encountered so far
            if price < min_price:
                min_price = price
        # Calculate the profit if selling at the current price
            profit = price - min_price
        # Update the maximum profit if current profit is higher
            if profit > max_profit:
                max_profit = profit

        return max_profit

solution =  Solution()
prices = [2,9,7,8,6,4,3,5,4,5,3,2,1]

output = solution.maxProfit(prices)
print(output)