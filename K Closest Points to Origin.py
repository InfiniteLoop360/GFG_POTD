from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        
        for x, y in points:
            distance = x**2 + y**2  
            heapq.heappush(min_heap, (distance, [x, y]))
        
        return [heapq.heappop(min_heap)[1] for _ in range(k)]
        
        
