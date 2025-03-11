class Solution:
    def countWays(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Initialize base cases
        a, b = 1, 2
        
        # Compute for n using iterative DP
        for _ in range(3, n + 1):
            a, b = b, a + b  # Shift values like Fibonacci series
        
        return b
