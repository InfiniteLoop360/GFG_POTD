import heapq
from collections import defaultdict

class Solution:
    def sumOfModes(self, arr, k):
        n = len(arr)
        if k == 0 or n == 0:
            return 0

        freq = defaultdict(int)
        heap = []  # stores (-frequency, value)

        def clean_top():
            # Pop stale entries until top reflects current freq
            while heap:
                fneg, val = heap[0]
                f = -fneg
                if freq.get(val, 0) == f:
                    return
                heapq.heappop(heap)

        # Build the first window
        for i in range(k):
            v = arr[i]
            freq[v] += 1
            heapq.heappush(heap, (-freq[v], v))

        clean_top()
        total = heap[0][1] if heap else 0

        # Slide the window
        for i in range(k, n):
            out = arr[i - k]
            # remove outgoing
            if out in freq:
                freq[out] -= 1
                if freq[out] == 0:
                    del freq[out]
                else:
                    heapq.heappush(heap, (-freq[out], out))

            # add incoming
            v = arr[i]
            freq[v] += 1
            heapq.heappush(heap, (-freq[v], v))

            clean_top()
            total += heap[0][1] if heap else 0

        return total
