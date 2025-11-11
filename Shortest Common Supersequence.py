class Solution:
    def minSuperSeq(self, s1, s2):
        n1, n2 = len(s1), len(s2)

        # Step 1: DP to compute LCS length
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Step 2: Apply the formula
        lcs_len = dp[n1][n2]
        return n1 + n2 - lcs_len
