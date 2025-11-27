class Solution:
    def subsetXORSum(self, arr):
        n = len(arr)
        OR = 0
        
        # Step 1: Compute OR of all elements
        for x in arr:
            OR |= x
        
        # Step 2: Result = OR * 2^(n-1)
        return OR * (1 << (n - 1))
