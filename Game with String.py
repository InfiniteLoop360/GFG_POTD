from collections import Counter
import heapq

class Solution:
    def minValue(self, s, k):
        freq = Counter(s)
        
        # Use max heap (invert values for heapq)
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)
        
        for _ in range(k):
            if max_heap:
                top = -heapq.heappop(max_heap)
                if top > 1:
                    heapq.heappush(max_heap, -(top - 1))

        # Sum of squares of frequencies
        return sum(x * x for x in map(lambda x: -x, max_heap))
