class Solution:
    def countConsec(self, n: int) -> int:
        # count of strings with no consecutive 1s
        if n == 0:
            return 0
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 2
        
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        total = 2 ** n
        return total - dp[n]
