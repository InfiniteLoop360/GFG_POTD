class Solution:
    def chocolatePickup(self, mat):
        n = len(mat)
        
        # If start or end is blocked, no valid path
        if mat[0][0] == -1 or mat[n-1][n-1] == -1:
            return 0
        
        # dp[k][i][p]:
        # k = total steps taken so far
        # i = row of person1
        # j = k-i (col of person1)
        # p = row of person2
        # q = k-p (col of person2)
        # Value = max chocolates collected
        dp = [[[-1]*(n) for _ in range(n)] for __ in range(2*n-1)]
        
        dp[0][0][0] = mat[0][0]  # starting point, both persons are at (0,0)
        
        for k in range(1, 2*n-1):
            for i in range(max(0, k-(n-1)), min(n-1, k)+1):
                j = k - i
                if j < 0 or j >= n or mat[i][j] == -1:
                    continue
                    
                for p in range(max(0, k-(n-1)), min(n-1, k)+1):
                    q = k - p
                    if q < 0 or q >= n or mat[p][q] == -1:
                        continue
                    
                    best = -1
                    # Four move combinations (down/down, right/right, down/right, right/down)
                    for di, dj in ((i-1, p-1), (i-1, p), (i, p-1), (i, p)):
                        if di >= 0 and dj >= 0:
                            best = max(best, dp[k-1][di][dj])
                    
                    if best < 0:
                        dp[k][i][p] = -1
                        continue
                    
                    chocolates = best + mat[i][j]
                    if (i, j) != (p, q):  # avoid double counting same cell
                        chocolates += mat[p][q]
                    
                    dp[k][i][p] = chocolates
        
        return max(0, dp[2*n-2][n-1][n-1])
