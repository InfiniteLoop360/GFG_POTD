class Solution:
    def maxWater(self, arr):
        n = len(arr)
        if n < 3:
            return 0
        
        left = [0] * n
        right = [0] * n
        
        # Fill left max array
        left[0] = arr[0]
        for i in range(1, n):
            left[i] = max(left[i - 1], arr[i])
        
        # Fill right max array
        right[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], arr[i])
        
        # Calculate water trapped
        water_trapped = 0
        for i in range(n):
            water_trapped += min(left[i], right[i]) - arr[i]
        
        return water_trapped
