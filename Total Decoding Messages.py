class Solution:
    def countWays(self, digits):
        # If the first character is '0', decoding is not possible
        if digits[0] == '0':
            return 0

        n = len(digits)
        dp = [0] * (n + 1)

        # Base Cases
        dp[0] = 1  # Empty string can be decoded in 1 way
        dp[1] = 1  # Single character (if not '0')

        for i in range(2, n + 1):
            # Single digit check (digits[i-1] should not be '0')
            if digits[i-1] != '0':
                dp[i] += dp[i-1]

            # Two-digit check (should be between 10 and 26)
            two_digit = int(digits[i-2:i])  # Convert substring to int
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]

        return dp[n]
