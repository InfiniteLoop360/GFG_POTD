class Solution:
    def cuts(self, s):
        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Base case: empty string needs 0 cuts

        for i in range(1, n + 1):
            for j in range(i):
                if s[j] != '0':  # No leading zero
                    substr = s[j:i]
                    num = int(substr, 2)
                    if num > 0 and self.is_power_of_5(num):
                        dp[i] = min(dp[i], dp[j] + 1)

        return dp[n] if dp[n] != float('inf') else -1

    def is_power_of_5(self, n):
        while n % 5 == 0:
            n //= 5
        return n == 1
