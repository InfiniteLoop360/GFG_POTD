class Solution:
    def nthRowOfPascalTriangle(self, n):
        row = [1]
        prev = 1
        for k in range(1, n):
            # Calculate next element based on the previous one
            next_val = prev * (n - k) // k
            row.append(next_val)
            prev = next_val
        return row
