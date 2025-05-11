import heapq
from typing import List

class Solution:
    def kthLargest(self, arr: List[int], k: int) -> int:
        n = len(arr)
        minHeap = []

        for i in range(n):
            sum_ = 0
            for j in range(i, n):
                sum_ += arr[j]

                if len(minHeap) < k:
                    heapq.heappush(minHeap, sum_)
                else:
                    if sum_ > minHeap[0]:
                        heapq.heappushpop(minHeap, sum_)

        return minHeap[0]
