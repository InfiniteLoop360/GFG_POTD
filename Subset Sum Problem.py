class Solution:
    def isSubsetSum(self, arr, target):
        n = len(arr)
        dp = [[False] * (target + 1) for _ in range(n + 1)]

        # Base case: A subset sum of 0 is always possible
        for i in range(n + 1):
            dp[i][0] = True

        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if arr[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]  # Cannot include arr[i-1]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]  # Include or exclude

        return dp[n][target]
