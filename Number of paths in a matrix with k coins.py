class Solution:
    def numberOfPath(self, mat, k):
        n = len(mat)
        m = len(mat[0])
        
        # dp[i][j][c] -> ways to reach cell (i, j) with c coins
        dp = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
        
        # Starting cell
        start_val = mat[0][0]
        if start_val <= k:
            dp[0][0][start_val] = 1
        
        # Fill DP table
        for i in range(n):
            for j in range(m):
                for c in range(k + 1):
                    if i == 0 and j == 0:
                        continue

                    current_val = mat[i][j]
                    if c >= current_val:
                        # From top
                        if i > 0:
                            dp[i][j][c] += dp[i - 1][j][c - current_val]
                        # From left
                        if j > 0:
                            dp[i][j][c] += dp[i][j - 1][c - current_val]
        
        return dp[n-1][m-1][k]
