class Solution:
    def findPeakGrid(self, mat):
        n = len(mat)
        m = len(mat[0])
        
        low, high = 0, m - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # Find row with maximum element in mid column
            maxRow = 0
            for i in range(n):
                if mat[i][mid] > mat[maxRow][mid]:
                    maxRow = i
            
            # Get left and right values
            left = mat[maxRow][mid - 1] if mid - 1 >= 0 else float('-inf')
            right = mat[maxRow][mid + 1] if mid + 1 < m else float('-inf')
            
            # Check peak condition
            if mat[maxRow][mid] >= left and mat[maxRow][mid] >= right:
                return [maxRow, mid]
            elif left > mat[maxRow][mid]:
                high = mid - 1
            else:
                low = mid + 1
        
        return [-1, -1]  # never reached logically
