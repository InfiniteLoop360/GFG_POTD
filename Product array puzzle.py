class Solution:
    def productExceptSelf(self, arr):
        n = len(arr)
        if n == 0:
            return []
        
        # Initialize prefix and suffix products
        prefix = [1] * n
        suffix = [1] * n
        result = [1] * n
        
        # Compute prefix product
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * arr[i - 1]
        
        # Compute suffix product
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * arr[i + 1]
        
        # Compute result using prefix and suffix arrays
        for i in range(n):
            result[i] = prefix[i] * suffix[i]
        
        return result
