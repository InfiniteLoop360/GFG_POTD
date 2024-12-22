class Solution:
    def matSearch(self, mat, x):
        # Start from the top-right corner
        n = len(mat)      # Number of rows
        m = len(mat[0])   # Number of columns
        
        row = 0
        col = m - 1

        while row < n and col >= 0:
            if mat[row][col] == x:
                return True
            elif mat[row][col] > x:
                col -= 1  # Move left
            else:
                row += 1  # Move down

        return False
