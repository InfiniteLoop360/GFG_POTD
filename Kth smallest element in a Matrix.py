class Solution:
    def kthSmallest(self, mat, k):
        n = len(mat)
        low, high = mat[0][0], mat[n-1][n-1]
        
        def count_less_equal(x):
            count = 0
            row, col = 0, n - 1
            
            while row < n and col >= 0:
                if mat[row][col] <= x:
                    count += col + 1
                    row += 1
                else:
                    col -= 1
            return count
        
        while low < high:
            mid = (low + high) // 2
            if count_less_equal(mid) < k:
                low = mid + 1
            else:
                high = mid
        
        return low
