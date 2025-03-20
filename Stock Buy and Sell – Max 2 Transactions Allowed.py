class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        # Initialize the four states
        buy1, sell1, buy2, sell2 = -float('inf'), 0, -float('inf'), 0
        
        for price in prices:
            # Update the states in order
            buy1 = max(buy1, -price)           # First buy
            sell1 = max(sell1, buy1 + price)   # First sell
            buy2 = max(buy2, sell1 - price)    # Second buy
            sell2 = max(sell2, buy2 + price)   # Second sell
        
        return sell2
