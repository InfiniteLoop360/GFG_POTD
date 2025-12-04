class Solution:
    def minCost(self, keys, freq):
        n = len(keys)

        # Prefix sum for fast frequency range sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + freq[i]

        # Function to get sum of freq[i...j]
        def getSum(i, j):
            return prefix[j + 1] - prefix[i]

        # dp[i][j] = Minimum cost of BST formed from keys i to j
        dp = [[0] * n for _ in range(n)]

        # Single key cost
        for i in range(n):
            dp[i][i] = freq[i]

        # Length of subtree
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')

                total_freq = getSum(i, j)

                # Try each key as root
                for r in range(i, j + 1):
                    left = dp[i][r - 1] if r > i else 0
                    right = dp[r + 1][j] if r < j else 0
                    dp[i][j] = min(dp[i][j], left + right + total_freq)

        return dp[0][n - 1]
