class Solution:
    def nCr(self, n, r):
        # Edge case: r > n means no combinations
        if r > n:
            return 0
        if r == 0 or r == n:
            return 1

        # Use iterative method to compute nCr efficiently
        r = min(r, n - r)  # Since C(n, r) == C(n, n - r)
        result = 1
        for i in range(r):
            result = result * (n - i) // (i + 1)

        return result
