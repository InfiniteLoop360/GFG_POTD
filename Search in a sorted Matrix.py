class Solution:
    # Function to search a given number in a strictly sorted matrix.
    def searchMatrix(self, mat, x):
        n = len(mat)    # Number of rows
        m = len(mat[0]) # Number of columns
        
        # Start searching from the top-right corner.
        i, j = 0, m - 1
        
        while i < n and j >= 0:
            if mat[i][j] == x:
                return True
            elif mat[i][j] > x:
                j -= 1  # Move left
            else:
                i += 1  # Move down
        
        return False  # If element is not found
