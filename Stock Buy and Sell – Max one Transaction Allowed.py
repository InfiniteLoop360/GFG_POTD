class Solution:
    def maximumProfit(self, prices):
        # Initialize the minimum price as the first element
        min_price = prices[0]
        max_profit = 0
        
        # Traverse the list of prices
        for price in prices:
            # If the current price is less than the minimum price seen so far, update min_price
            if price < min_price:
                min_price = price
            # If the current price minus min_price gives a higher profit, update max_profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit
