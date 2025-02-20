import heapq

class Solution:
    def getMedian(self, arr):
        min_heap = []  # Min-Heap (stores larger half)
        max_heap = []  # Max-Heap (stores smaller half, inverted to act as max heap)
        medians = []

        for num in arr:
            # Step 1: Insert into max heap (negative for min heap simulation)
            heapq.heappush(max_heap, -num)
            
            # Step 2: Balance - Ensure max_heap's top is always <= min_heap's top
            if max_heap and min_heap and (-max_heap[0] > min_heap[0]):
                heapq.heappush(min_heap, -heapq.heappop(max_heap))

            # Step 3: Balance the size difference (at most 1)
            if len(max_heap) > len(min_heap) + 1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            elif len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))

            # Step 4: Compute the median
            if len(max_heap) > len(min_heap):
                medians.append(float(-max_heap[0]))  # Max-Heap top
            else:
                medians.append((-max_heap[0] + min_heap[0]) / 2.0)  # Average of tops

        return medians
