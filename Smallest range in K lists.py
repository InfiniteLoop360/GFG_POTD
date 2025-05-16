import heapq

class Solution:
    def findSmallestRange(self, arr):
        k = len(arr)
        n = len(arr[0])
        
        # min_heap contains (value, row_index, col_index)
        min_heap = []
        max_val = float('-inf')
        
        # Step 1: Push the first element from each list
        for i in range(k):
            heapq.heappush(min_heap, (arr[i][0], i, 0))
            max_val = max(max_val, arr[i][0])
        
        # Initialize the smallest range
        range_start, range_end = -1e5, 1e5
        
        while True:
            min_val, row, col = heapq.heappop(min_heap)
            
            # Update range if smaller
            if max_val - min_val < range_end - range_start:
                range_start, range_end = min_val, max_val
            
            # Move to next element in the same list
            if col + 1 < n:
                next_val = arr[row][col + 1]
                heapq.heappush(min_heap, (next_val, row, col + 1))
                max_val = max(max_val, next_val)
            else:
                # One of the lists is exhausted
                break
        
        return [range_start, range_end]
