class Solution:
    
    # Function to search a given number in row-column sorted matrix.
    def searchRowMatrix(self, mat, x): 
        n = len(mat)     # Number of rows
        m = len(mat[0])  # Number of columns

        for row in mat:
            if x in row:
                return True
        return False
