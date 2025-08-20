class Solution:
    def searchMatrix(self, mat, x):
        n, m = len(mat), len(mat[0])
        left, right = 0, n * m - 1
        
        while left <= right:
            mid = (left + right) // 2
            row, col = divmod(mid, m)
            mid_val = mat[row][col]
            
            if mid_val == x:
                return True
            
            # Left half sorted
            left_row, left_col = divmod(left, m)
            right_row, right_col = divmod(right, m)
            
            if mat[left_row][left_col] <= mid_val:
                if mat[left_row][left_col] <= x < mid_val:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if mid_val < x <= mat[right_row][right_col]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False
