class Solution:
    def rowWithMax1s(self, arr):
        n = len(arr)
        m = len(arr[0])
        
        row_index = -1
        j = m - 1  # start from top-right
        
        for i in range(n):
            while j >= 0 and arr[i][j] == 1:
                j -= 1
                row_index = i
        
        return row_index
