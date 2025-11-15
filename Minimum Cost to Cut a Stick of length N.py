class Solution:
    def minCutCost(self, n, cuts):
        cuts = sorted(cuts)
        # Add boundaries 0 and n
        arr = [0] + cuts + [n]
        m = len(arr)

        # dp[i][j] = minimum cost to cut stick from arr[i] to arr[j]
        dp = [[0] * m for _ in range(m)]

        # length is interval size
        for length in range(2, m):    
            for i in range(0, m - length):
                j = i + length
                dp[i][j] = float('inf')

                # Try every possible cut between i and j
                for k in range(i + 1, j):
                    cost = arr[j] - arr[i] + dp[i][k] + dp[k][j]
                    dp[i][j] = min(dp[i][j], cost)

        return dp[0][m - 1]
