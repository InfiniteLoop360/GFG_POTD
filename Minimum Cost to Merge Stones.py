class Solution:
    def mergeStones(self, stones, k):
        n = len(stones)
        # Feasibility check
        if (n - 1) % (k - 1) != 0:
            return -1

        # Prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + stones[i]

        def range_sum(i, j):
            return prefix[j+1] - prefix[i]

        # dp[i][j] = min cost to merge stones[i..j] into as few piles as possible
        INF = 10**18
        dp = [[0 if i == j else INF for j in range(n)] for i in range(n)]

        # len is interval length
        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                dp[i][j] = INF
                # try all valid splits; stepping by k-1 reduces unnecessary partitions
                m = i
                while m < j:
                    dp[i][j] = min(dp[i][j], dp[i][m] + dp[m+1][j])
                    m += (k - 1)
                # if we can merge the whole interval into 1 pile, add sum
                if (length - 1) % (k - 1) == 0:
                    dp[i][j] += range_sum(i, j)

        return dp[0][n-1]
