class Solution:
    def LCIS(self, a, b):
        n, m = len(a), len(b)
        dp = [0] * m   # dp[j] = LCIS ending at b[j]

        for i in range(n):
            current = 0  # best LCIS so far for all b[j] < a[i]
            for j in range(m):
                if a[i] == b[j]:
                    dp[j] = max(dp[j], current + 1)
                elif a[i] > b[j]:
                    current = max(current, dp[j])
        return max(dp)
