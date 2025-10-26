import heapq

class Solution:
    def minCost(self, arr):
        # If only one rope, no cost needed
        if len(arr) <= 1:
            return 0
        
        # Create a min-heap
        heapq.heapify(arr)
        
        total_cost = 0
        
        # Keep connecting ropes until one remains
        while len(arr) > 1:
            # Pop two smallest
            first = heapq.heappop(arr)
            second = heapq.heappop(arr)
            
            # Calculate cost
            cost = first + second
            total_cost += cost
            
            # Push the new rope back
            heapq.heappush(arr, cost)
        
        return total_cost
