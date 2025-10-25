import heapq

class Solution:
    def minOperations(self, arr):
        total_sum = sum(arr)
        target = total_sum / 2
        current_sum = total_sum

        # Convert to max heap (store negative)
        max_heap = [-x for x in arr]
        heapq.heapify(max_heap)

        ops = 0

        while current_sum > target:
            # Get largest element
            largest = -heapq.heappop(max_heap)
            half = largest / 2

            # Reduce the sum by this halving
            current_sum -= half

            # Push halved value back
            heapq.heappush(max_heap, -half)

            ops += 1

        return ops
