import math

class Solution:
    def minTime(self, ranks, n):
        
        low = 0
        high = max(ranks) * n * (n + 1) // 2
        
        def canMake(time):
            donuts = 0
            for r in ranks:
                # Solve r * (k*(k+1)//2) <= time
                # k^2 + k - (2*time/r) <= 0
                val = int((math.sqrt(1 + 8 * time // r) - 1) // 2)
                donuts += val
                if donuts >= n:
                    return True
            return False
        
        while low < high:
            mid = (low + high) // 2
            if canMake(mid):
                high = mid
            else:
                low = mid + 1
        
        return low
