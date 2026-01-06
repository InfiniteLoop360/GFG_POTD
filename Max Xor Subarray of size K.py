class Solution:
    def maxSubarrayXOR(self, arr, k):
        window_xor = 0
        for i in range(k):
            window_xor ^= arr[i]
        
        max_xor = window_xor
        
        for i in range(k, len(arr)):
            window_xor ^= arr[i - k] 
            window_xor ^= arr[i]      
            max_xor = max(max_xor, window_xor)
        
        return max_xor
