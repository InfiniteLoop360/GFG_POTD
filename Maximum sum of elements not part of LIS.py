class Solution:
    def nonLisMaxSum(self, arr):
        n = len(arr)
        dp = [1] * n              # dp[i]: length of LIS ending at i
        sum_dp = arr[:]           # sum_dp[i]: min sum of LIS ending at i

        for i in range(n):
            for j in range(i):
                if arr[j] < arr[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        sum_dp[i] = sum_dp[j] + arr[i]
                    elif dp[j] + 1 == dp[i]:
                        sum_dp[i] = min(sum_dp[i], sum_dp[j] + arr[i])

        max_len = max(dp)
        min_lis_sum = float('inf')

        for i in range(n):
            if dp[i] == max_len:
                min_lis_sum = min(min_lis_sum, sum_dp[i])

        total_sum = sum(arr)
        return total_sum - min_lis_sum
