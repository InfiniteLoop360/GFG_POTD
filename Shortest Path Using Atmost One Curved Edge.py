import heapq

class Solution:
    def shortestPath(self, V, a, b, edges):
        # Build adjacency list for straight edges only (w1).
        # Use 0-based vertices as given.
        adj = [[] for _ in range(V)]
        # Keep curved edges separate to evaluate later
        curved_edges = []
        for u, v, w1, w2 in edges:
            # add straight (undirected)
            adj[u].append((v, w1))
            adj[v].append((u, w1))
            # store curved edges (undirected but we will check both directions)
            curved_edges.append((u, v, w2))

        INF = 10**30

        def dijkstra(start):
            dist = [INF] * V
            dist[start] = 0
            heap = [(0, start)]
            while heap:
                d, node = heapq.heappop(heap)
                if d != dist[node]:
                    continue
                # early stop not useful since we need full dist array
                for nei, w in adj[node]:
                    nd = d + w
                    if nd < dist[nei]:
                        dist[nei] = nd
                        heapq.heappush(heap, (nd, nei))
            return dist

        # If a == b, answer is 0 trivially (no movement needed)
        if a == b:
            return 0

        dist_a = dijkstra(a)
        dist_b = dijkstra(b)  # dist from b to all nodes (since graph is undirected)

        # Start with the option of taking zero curved edges
        best = dist_a[b]

        # Try all curved edges (both directions)
        for u, v, w2 in curved_edges:
            # a -> u (straight-only) + curved u->v + v -> b (straight-only)
            if dist_a[u] < INF and dist_b[v] < INF:
                best = min(best, dist_a[u] + w2 + dist_b[v])
            # a -> v (straight-only) + curved v->u + u -> b (straight-only)
            if dist_a[v] < INF and dist_b[u] < INF:
                best = min(best, dist_a[v] + w2 + dist_b[u])

        if best >= INF:
            return -1
        return best
