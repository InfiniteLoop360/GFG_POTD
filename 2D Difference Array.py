class Solution:
    def applyDiff2D(self, mat, opr):
        n = len(mat)
        m = len(mat[0])
        
        # Initialize a 2D diff matrix with one extra row and col
        diff = [[0] * (m + 2) for _ in range(n + 2)]
        
        # Apply each operation in constant time
        for v, r1, c1, r2, c2 in opr:
            diff[r1][c1] += v
            diff[r1][c2 + 1] -= v
            diff[r2 + 1][c1] -= v
            diff[r2 + 1][c2 + 1] += v
        
        # Convert diff matrix into actual update matrix using prefix sums
        for i in range(n):
            for j in range(m):
                if i > 0:
                    diff[i][j] += diff[i - 1][j]
                if j > 0:
                    diff[i][j] += diff[i][j - 1]
                if i > 0 and j > 0:
                    diff[i][j] -= diff[i - 1][j - 1]
        
        # Apply the difference values to the original matrix
        for i in range(n):
            for j in range(m):
                mat[i][j] += diff[i][j]
        
        return mat
