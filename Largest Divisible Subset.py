class Solution:
    def largestSubset(self, arr):
        n = len(arr)
        arr.sort()
        dp = [[] for _ in range(n)]
        max_subset = []

        for i in range(n):
            max_prev = []
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    if len(dp[j]) > len(max_prev) or (len(dp[j]) == len(max_prev) and dp[j] > max_prev):
                        max_prev = dp[j]
            dp[i] = max_prev + [arr[i]]
            if len(dp[i]) > len(max_subset) or (len(dp[i]) == len(max_subset) and dp[i] > max_subset):
                max_subset = dp[i]

        return max_subset
