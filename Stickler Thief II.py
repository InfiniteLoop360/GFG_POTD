class Solution:
    def maxValue(self, arr):
        if len(arr) == 1:
            return arr[0]  # Only one house, loot it
        
        def robLinear(arr, start, end):
            prev1, prev2 = 0, 0
            for i in range(start, end + 1):
                curr = max(prev1, arr[i] + prev2)
                prev2, prev1 = prev1, curr
            return prev1
        
        return max(robLinear(arr, 0, len(arr) - 2), robLinear(arr, 1, len(arr) - 1))
