class Solution:
    def findMaxSum(self, arr):
        if not arr: return 0
        if len(arr) == 1: return arr[0]
        
        prev2 = arr[0]  # dp[i-2]
        prev1 = max(arr[0], arr[1])  # dp[i-1]
        
        for i in range(2, len(arr)):
            curr = max(prev1, arr[i] + prev2)  # dp[i] = max(dp[i-1], arr[i] + dp[i-2])
            prev2 = prev1  # Move dp[i-2] forward
            prev1 = curr  # Move dp[i-1] forward
        
        return prev1
