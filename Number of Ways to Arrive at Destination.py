import heapq

class Solution:
    def countPaths(self, V, edges):
        MOD = 10**9 + 7

        # Build adjacency list
        adj = [[] for _ in range(V)]
        for u, v, t in edges:
            adj[u].append((v, t))
            adj[v].append((u, t))

        # distances and ways
        INF = 10**18
        dist = [INF] * V
        ways = [0] * V

        dist[0] = 0
        ways[0] = 1

        pq = [(0, 0)]  # (distance, node)
        while pq:
            d, u = heapq.heappop(pq)
            # If we've already found a better way to u, skip
            if d > dist[u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    ways[v] = ways[u]
                    heapq.heappush(pq, (nd, v))
                elif nd == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD

        return ways[V-1] % MOD
