class Solution:
    def findMinCycle(self, V, edges):
        INF = 10**9
        # Step 1: Initialize distance matrix
        dist = [[INF] * V for _ in range(V)]
        
        # Adjacency matrix to store edge weights
        adj = [[INF] * V for _ in range(V)]
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
            adj[u][v] = w
            adj[v][u] = w

        min_cycle = INF

        # Step 2: Floyd-Warshall with cycle detection
        for k in range(V):
            # Check for cycle involving node k
            for i in range(k):
                for j in range(i + 1, k):
                    if dist[i][j] != INF and adj[i][k] != INF and adj[k][j] != INF:
                        cycle_weight = dist[i][j] + adj[i][k] + adj[k][j]
                        min_cycle = min(min_cycle, cycle_weight)

            # Standard Floyd-Warshall update
            for i in range(V):
                for j in range(V):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        return -1 if min_cycle == INF else min_cycle
