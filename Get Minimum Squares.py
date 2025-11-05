class Solution:
    def minSquares(self, n):
        # dp[x] = minimum number of perfect squares needed to form x
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        # Pre-calc perfect squares up to n
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1
        
        # Bottom-up DP
        for x in range(1, n + 1):
            for sq in squares:
                if sq > x:
                    break
                dp[x] = min(dp[x], 1 + dp[x - sq])
        
        return dp[n]
