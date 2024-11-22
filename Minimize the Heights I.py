class Solution:
    def getMinDiff(self, k, arr):
        # Sort the array
        arr.sort()
        n = len(arr)
        
        # Initial difference between the largest and smallest values
        result = arr[-1] - arr[0]
        
        # Iterate through the array and try to minimize the difference
        for i in range(n - 1):
            # Current maximum and minimum heights
            max_height = max(arr[-1] - k, arr[i] + k)
            min_height = min(arr[0] + k, arr[i + 1] - k)
            
            # Update the result with the minimum difference found
            result = min(result, max_height - min_height)
        
        return result
