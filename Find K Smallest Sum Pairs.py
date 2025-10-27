import heapq

class Solution:
    def kSmallestPair(self, arr1, arr2, k):
        """
        Return list of up to k pairs [a,b] from arr1 x arr2 with smallest sums.
        Both arr1 and arr2 are sorted ascending.
        """
        if k <= 0 or not arr1 or not arr2:
            return []

        n1, n2 = len(arr1), len(arr2)
        # We only need first min(k, n1) rows
        r = min(k, n1)

        # min-heap entries: (sum, i, j)
        heap = []
        for i in range(r):
            heap.append((arr1[i] + arr2[0], i, 0))
        heapq.heapify(heap)

        result = []
        while heap and len(result) < k:
            s, i, j = heapq.heappop(heap)
            result.append([arr1[i], arr2[j]])
            # push next element in the same row (i, j+1)
            if j + 1 < n2:
                heapq.heappush(heap, (arr1[i] + arr2[j+1], i, j+1))

        return result
