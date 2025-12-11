import math

class Solution:
    def constructArr(self, arr):
        # 1. Calculate the size of the original array (n)
        # Length of arr (L) = n * (n - 1) / 2
        # This results in quadratic equation: n^2 - n - 2*L = 0
        L = len(arr)
        delta = 1 + 8 * L
        n = (1 + int(delta**0.5)) // 2
        
        # 2. Handle Edge Case: n = 2
        # If n=2, we only have one sum (res[0] + res[1]).
        # There are infinite solutions, but typically a split is accepted.
        if n == 2:
            val = arr[0] // 2
            return [val, arr[0] - val]
            
        # 3. Solve for res[0] using the 'Triangle' of sums
        # We know:
        # arr[0]   = res[0] + res[1]
        # arr[1]   = res[0] + res[2]
        # arr[n-1] = res[1] + res[2]  <-- This is the first pair NOT involving res[0]
        
        sum_0_1 = arr[0]
        sum_0_2 = arr[1]
        sum_1_2 = arr[n-1]
        
        # Logic: ( (res[0]+res[1]) + (res[0]+res[2]) - (res[1]+res[2]) ) / 2  = res[0]
        res0 = (sum_0_1 + sum_0_2 - sum_1_2) // 2
        
        # 4. Construct the result array
        res = [0] * n
        res[0] = res0
        
        # Fill the rest of the array using the first 'n-1' elements of pair-sums
        # Since arr[i-1] = res[0] + res[i] for i = 1 to n-1
        for i in range(1, n):
            res[i] = arr[i-1] - res0
            
        return res
