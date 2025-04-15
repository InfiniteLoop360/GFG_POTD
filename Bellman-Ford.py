class Solution:
    def bellmanFord(self, V, edges, src):
        # Step 1: Initialize distances
        dist = [float('inf')] * V
        dist[src] = 0
        
        # Step 2: Relax all edges (V-1) times
        for i in range(V - 1):
            for u, v, wt in edges:
                if dist[u] != float('inf') and dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt
        
        # Step 3: Check for negative weight cycles
        for u, v, wt in edges:
            if dist[u] != float('inf') and dist[u] + wt < dist[v]:
                return [-1]  # Negative weight cycle detected

        # Step 4: Replace 'inf' with 1e8 for unreachable vertices
        return [int(d) if d != float('inf') else int(1e8) for d in dist]
