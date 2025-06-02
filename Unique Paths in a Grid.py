class Solution:
    def uniquePaths(self, grid):
        n = len(grid)
        m = len(grid[0])
        
        if grid[0][0] == 1 or grid[n-1][m-1] == 1:
            return 0

        dp = [0] * m
        for i in range(n):
            new_dp = [0] * m
            for j in range(m):
                if grid[i][j] == 1:
                    new_dp[j] = 0
                elif i == 0 and j == 0:
                    new_dp[j] = 1
                else:
                    up = dp[j] if i > 0 else 0
                    left = new_dp[j - 1] if j > 0 else 0
                    new_dp[j] = up + left
            dp = new_dp
        
        return dp[-1]
