from collections import Counter
import heapq

class Solution:
    def topKFreq(self, arr, k):
        # Step 1: Count frequency of each element
        freq = Counter(arr)

        # Step 2: Use a max-heap (negative frequency because heapq is min-heap)
        # Priority: higher frequency first, if tie -> larger number first
        heap = [(-f, -num) for num, f in freq.items()]
        heapq.heapify(heap)

        # Step 3: Extract top k elements
        res = []
        for _ in range(k):
            f, num = heapq.heappop(heap)
            res.append(-num)
        
        return res
