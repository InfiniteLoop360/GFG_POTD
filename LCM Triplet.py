import math
from itertools import combinations

class Solution:
    def lcmTriplets(self, n):
        def lcm(a, b):
            return a * b // math.gcd(a, b)
        
        def lcm3(a, b, c):
            return lcm(lcm(a, b), c)
        
        max_lcm = 0
        # If n is less than or equal to 2, just return the product
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 6

        # Try combinations among top 5 numbers only
        for a in range(n, n - 5, -1):
            for b in range(n, n - 5, -1):
                for c in range(n, n - 5, -1):
                    if a >= b >= c:
                        max_lcm = max(max_lcm, lcm3(a, b, c))
        return max_lcm
