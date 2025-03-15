'''
Dynamic Programming (Tabulation) - Bottom-Up
'''

class Solution:
    def minCoins(self, coins, sum):
        # Initialize dp array with a large value
        dp = [float('inf')] * (sum + 1)
        dp[0] = 0  # Base case: 0 coins needed to make sum = 0

        for coin in coins:
            for j in range(coin, sum + 1):
                dp[j] = min(dp[j], 1 + dp[j - coin])

        return dp[sum] if dp[sum] != float('inf') else -1


'''
Recursion + Memoization (Top-Down)
A recursive approach with memoization (caching) can also solve the problem efficiently.

🔹 Recursive Formula:
minCoins(sum) = min(1 + minCoins(sum - coin)) for all coin in coins

'''
class Solution:
    def minCoins(self, coins, sum):
        memo = {}

        def helper(s):
            if s == 0:
                return 0  # Base case: 0 coins needed for sum = 0
            if s < 0:
                return float('inf')  # Impossible case
            if s in memo:
                return memo[s]

            min_coins = float('inf')
            for coin in coins:
                min_coins = min(min_coins, 1 + helper(s - coin))

            memo[s] = min_coins
            return min_coins

        ans = helper(sum)
        return ans if ans != float('inf') else -1


