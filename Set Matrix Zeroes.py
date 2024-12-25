class Solution:
    def setMatrixZeroes(self, mat):
        n = len(mat)
        m = len(mat[0])
        
        # Flag to check if the first row and first column need to be set to zero
        first_row_zero = False
        first_col_zero = False
        
        # Check if the first row has any zeroes
        for j in range(m):
            if mat[0][j] == 0:
                first_row_zero = True
                break
        
        # Check if the first column has any zeroes
        for i in range(n):
            if mat[i][0] == 0:
                first_col_zero = True
                break
        
        # Use the first row and first column to mark the cells to be zeroed
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][j] == 0:
                    mat[i][0] = 0  # Mark the first column
                    mat[0][j] = 0  # Mark the first row
        
        # Set the cells to zero using the markers
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][0] == 0 or mat[0][j] == 0:
                    mat[i][j] = 0
        
        # Handle the first row
        if first_row_zero:
            for j in range(m):
                mat[0][j] = 0
        
        # Handle the first column
        if first_col_zero:
            for i in range(n):
                mat[i][0] = 0
