class Solution:
    def subarrayXor(self, arr):
        n = len(arr)
        ans = 0
        
        for i in range(n):
            count = (i + 1) * (n - i)
            
            if count % 2 == 1:
                ans ^= arr[i]
        
        return ans
