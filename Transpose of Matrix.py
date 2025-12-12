class Solution:
    def transpose(self, mat):
        n = len(mat)
        
        # Transpose in-place
        for i in range(n):
            for j in range(i+1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        
        return mat
