import heapq

class Solution:
    def minCost(self, houses):
        n = len(houses)
        inMST = [False] * n
        minHeap = [(0, 0)]  
        minCost = 0
        connected = 0

        while connected < n:
            cost, u = heapq.heappop(minHeap)
            if inMST[u]:
                continue
            inMST[u] = True
            minCost += cost
            connected += 1

            for v in range(n):
                if not inMST[v]:
                    dist = abs(houses[u][0] - houses[v][0]) + abs(houses[u][1] - houses[v][1])
                    heapq.heappush(minHeap, (dist, v))

        return minCost
