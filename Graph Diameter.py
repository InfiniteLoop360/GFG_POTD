from collections import deque

class Solution:
    def diameter(self, V, edges):
        # Build adjacency list
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Helper BFS: returns (farthest_node, distance_to_that_node)
        def bfs(start):
            dist = [-1] * V
            q = deque()
            q.append(start)
            dist[start] = 0
            farthest_node = start
            maxd = 0
            while q:
                node = q.popleft()
                dnode = dist[node]
                # Update farthest
                if dnode > maxd:
                    maxd = dnode
                    farthest_node = node
                for nei in adj[node]:
                    if dist[nei] == -1:
                        dist[nei] = dnode + 1
                        q.append(nei)
            return farthest_node, maxd

        # First BFS from any node (0)
        # Graph is connected per problem statement, but handle V==0/1
        if V == 0:
            return 0
        # Start from node 0 (or any node)
        node_u, _ = bfs(0)
        # BFS from node_u to get diameter
        _, diameter = bfs(node_u)
        return diameter
