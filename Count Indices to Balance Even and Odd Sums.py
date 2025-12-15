class Solution:
    def cntWays(self, arr):
        n = len(arr)
        
        # Step 1: Compute prefix sums
        evenPrefix = [0] * n
        oddPrefix = [0] * n
        
        for i in range(n):
            if i % 2 == 0:
                evenPrefix[i] = arr[i] + (evenPrefix[i-1] if i > 0 else 0)
                oddPrefix[i] = oddPrefix[i-1] if i > 0 else 0
            else:
                oddPrefix[i] = arr[i] + (oddPrefix[i-1] if i > 0 else 0)
                evenPrefix[i] = evenPrefix[i-1]
        
        totalEven = evenPrefix[-1]
        totalOdd = oddPrefix[-1]
        
        # Step 2: Count valid indices
        count = 0
        for i in range(n):
            evenBefore = evenPrefix[i-1] if i > 0 else 0
            oddBefore = oddPrefix[i-1] if i > 0 else 0
            
            oddAfter = totalOdd - oddPrefix[i]
            evenAfter = totalEven - evenPrefix[i]
            
            newEvenSum = evenBefore + oddAfter
            newOddSum = oddBefore + evenAfter
            
            if newEvenSum == newOddSum:
                count += 1
        
        return count
