class Solution:
    def maxGold(self, mat):
        if not mat or not mat[0]:
            return 0

        n = len(mat)
        m = len(mat[0])

        # Create DP table same size as mat
        dp = [[0] * m for _ in range(n)]

        # Fill the last column as base case
        for i in range(n):
            dp[i][m - 1] = mat[i][m - 1]

        # Fill the table from second-last column to first
        for j in range(m - 2, -1, -1):
            for i in range(n):
                # Right
                right = dp[i][j + 1]

                # Right-Up
                right_up = dp[i - 1][j + 1] if i > 0 else 0

                # Right-Down
                right_down = dp[i + 1][j + 1] if i < n - 1 else 0

                dp[i][j] = mat[i][j] + max(right, right_up, right_down)

        # Maximum in first column is the answer
        return max(dp[i][0] for i in range(n))
