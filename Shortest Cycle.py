from collections import deque

class Solution:
    def shortCycle(self, V, edges):
        """
        Return length (number of edges) of the shortest cycle in an undirected graph.
        If none, return -1.
        V: number of vertices (0..V-1)
        edges: list of [u, v] undirected edges
        """
        if V <= 0:
            return -1

        # Build adjacency list
        adj = [[] for _ in range(V)]
        for u, v in edges:
            # guard: avoid duplicate insertions if input repeats edges,
            # but duplicates are OK; we'll keep them.
            adj[u].append(v)
            adj[v].append(u)

        INF = 10**9
        ans = INF

        # BFS from every start vertex
        for start in range(V):
            # If current best is 3, can't improve below 3 (min possible >= 3 except for parallel edges)
            # but we still must consider cycles of length 1 or 2 (self loop or multiedge).
            # To detect cycles of length 1 or 2 quickly, we can pre-scan:
            # However we'll rely on BFS to find them too.
            dist = [-1] * V
            parent = [-1] * V
            q = deque([start])
            dist[start] = 0
            # Regular BFS
            while q:
                u = q.popleft()
                # Small pruning: if dist[u] * 2 + 1 >= ans, deeper nodes from u won't produce better cycles
                # because any cycle involving deeper node will have length >= dist[u] + dist[v] + 1 >= 2*dist[u] + 1.
                # This is safe but optional; uncomment to enable pruning:
                # if dist[u] * 2 + 1 >= ans:
                #     continue

                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        parent[v] = u
                        q.append(v)
                    elif parent[u] != v:
                        # found a cycle: length = dist[u] + dist[v] + 1
                        cycle_len = dist[u] + dist[v] + 1
                        if cycle_len < ans:
                            ans = cycle_len
                # early exit: shortest possible cycle is 3 (triangle) unless multiedges exist.
                # If ans == 3 we can't do better (unless we allow length 2 from multi-edge or 1 from self-loop).
                # so we can break early if ans == 3.
                # But keep searching if multiedges/self-loops possible.
            # small global early stop
            if ans == 3:  # 3 is minimal simple cycle in simple undirected graph
                break

        return -1 if ans == INF else ans
