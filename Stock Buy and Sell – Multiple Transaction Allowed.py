from typing import List

class Solution:
    def maximumProfit(self, prices: List[int]) -> int:
        profit = 0
        
        # Traverse the list of prices from the second day onwards
        for i in range(1, len(prices)):
            # If the price of the next day is greater than the current day
            if prices[i] > prices[i - 1]:
                # Add the difference (profit) to the total profit
                profit += prices[i] - prices[i - 1]
        
        return profit
