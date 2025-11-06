class Solution:
    def numberOfWays(self, n):
        if n <= 2:
            return n
        
        prev2, prev1 = 1, 2  # dp[1] = 1, dp[2] = 2
        
        for i in range(3, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        
        return prev1
