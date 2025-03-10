class Solution:
    def editDistance(self, s1, s2):
        n, m = len(s1), len(s2)

        # Create a DP table where dp[i][j] represents the minimum operations needed 
        # to convert s1[0...i-1] to s2[0...j-1]
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Fill the DP table
        for i in range(n + 1):
            for j in range(m + 1):

                # Case 1: If s1 is empty, we need to insert all characters of s2
                if i == 0:
                    dp[i][j] = j  

                # Case 2: If s2 is empty, we need to delete all characters of s1
                elif j == 0:
                    dp[i][j] = i  

                # Case 3: If last characters match, no operation needed
                elif s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

                # Case 4: If last characters don't match, consider three operations:
                # Insert, Remove, Replace, and take the minimum among them
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1],    # Insert
                                       dp[i - 1][j],    # Remove
                                       dp[i - 1][j - 1])  # Replace

        # The final answer is stored at dp[n][m]
        return dp[n][m]

