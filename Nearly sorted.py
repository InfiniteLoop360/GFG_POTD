import heapq

class Solution:
    def nearlySorted(self, arr, k):
        n = len(arr)
        heap = []
        
        # Step 1: Push first k+1 elements into the heap
        for i in range(min(k + 1, n)):
            heapq.heappush(heap, arr[i])
        
        index = 0
        
        # Step 2: For remaining elements
        for i in range(k + 1, n):
            arr[index] = heapq.heappop(heap)
            index += 1
            heapq.heappush(heap, arr[i])
        
        # Step 3: Pop remaining elements
        while heap:
            arr[index] = heapq.heappop(heap)
            index += 1
        
        return arr
