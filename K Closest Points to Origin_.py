import heapq

class Solution:
    def kClosest(self, points, k):
        # Max heap to store k closest points
        heap = []
        
        for (x, y) in points:
            dist = x*x + y*y
            heapq.heappush(heap, (-dist, x, y))
            
            # If heap exceeds size k, remove farthest
            if len(heap) > k:
                heapq.heappop(heap)
                
        # Extract k points
        result = [[x, y] for (_, x, y) in heap]
        return result
