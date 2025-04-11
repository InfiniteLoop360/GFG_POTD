import heapq

class Solution:
    def dijkstra(self, V, edges, src):
        from collections import defaultdict
        
        # Step 1: Build adjacency list
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))  # Undirected graph
        
        # Step 2: Initialize
        dist = [float('inf')] * V
        dist[src] = 0
        heap = [(0, src)]  # (distance, node)

        while heap:
            d, u = heapq.heappop(heap)

            for v, w in graph[u]:
                if dist[v] > d + w:
                    dist[v] = d + w
                    heapq.heappush(heap, (dist[v], v))
        
        return dist
