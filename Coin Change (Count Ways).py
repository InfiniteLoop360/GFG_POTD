class Solution:
    def count(self, coins, sum):
        # Initialize DP array with size (sum + 1), all set to 0
        dp = [0] * (sum + 1)
        
        # Base case: One way to make sum 0 (by taking no coins)
        dp[0] = 1

        # Iterate over each coin
        for coin in coins:
            for j in range(coin, sum + 1):
                dp[j] += dp[j - coin]

        return dp[sum]
