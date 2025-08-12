class Solution:
    def minMaxCandy(self, prices, k):
        n = len(prices)

        # -------- Minimum Cost --------
        prices.sort()
        min_cost = 0
        left, right = 0, n - 1
        while left <= right:
            # Buy the cheapest one
            min_cost += prices[left]
            left += 1
            # Take k most expensive remaining for free
            right -= k

        # -------- Maximum Cost --------
        prices.sort(reverse=True)
        max_cost = 0
        left, right = 0, n - 1
        while left <= right:
            # Buy the most expensive one
            max_cost += prices[left]
            left += 1
            # Take k cheapest remaining for free
            right -= k

        return [min_cost, max_cost]
