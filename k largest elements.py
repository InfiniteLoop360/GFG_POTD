#Min-Heap (Efficient for Large Inputs)

import heapq

class Solution:
    def kLargest(self, arr, k):
        # Step 1: Create a min-heap of the first k elements
        min_heap = arr[:k]
        heapq.heapify(min_heap)  # Convert into a min-heap

        # Step 2: Process the rest of the array
        for num in arr[k:]:
            if num > min_heap[0]:  # Compare with the smallest in heap
                heapq.heappop(min_heap)  # Remove smallest
                heapq.heappush(min_heap, num)  # Add new element

        # Step 3: Extract k largest elements and sort in descending order
        return sorted(min_heap, reverse=True)


#Alternative Approach: Sorting (Less Efficient)

class Solution:
    def kLargest(self, arr, k):
        return sorted(arr, reverse=True)[:k]
