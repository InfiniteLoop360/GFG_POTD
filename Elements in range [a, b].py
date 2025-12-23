from bisect import bisect_left, bisect_right

class Solution:
    def cntInRange(self, arr, queries):
        # Step 1: Sort the array (MANDATORY)
        arr.sort()
        
        result = []
        
        # Step 2: Process each query
        for L, R in queries:
            left = bisect_left(arr, L)   # first value >= L
            right = bisect_right(arr, R) # first value > R
            
            result.append(right - left)
        
        return result
