class Solution:
    def maxRectSum(self, mat):
        if not mat or not mat[0]:
            return 0

        n = len(mat)
        m = len(mat[0])
        max_sum = float('-inf')

        for top in range(n):
            temp = [0] * m  # Compressed column sums

            for bottom in range(top, n):
                for col in range(m):
                    temp[col] += mat[bottom][col]

                # Apply Kadane’s Algorithm on temp
                max_sum = max(max_sum, self.kadane(temp))

        return max_sum

    def kadane(self, arr):
        max_end_here = max_so_far = arr[0]
        for x in arr[1:]:
            max_end_here = max(x, max_end_here + x)
            max_so_far = max(max_so_far, max_end_here)
        return max_so_far
