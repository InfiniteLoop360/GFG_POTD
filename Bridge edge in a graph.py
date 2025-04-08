class Solution:
    def isBridge(self, V, edges, c, d):
        from collections import defaultdict

        # Step 1: Build the graph
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Step 2: DFS without the (c, d) edge
        def dfs(node, visited):
            visited[node] = True
            for neighbor in adj[node]:
                # Skip the edge we are testing
                if (node == c and neighbor == d) or (node == d and neighbor == c):
                    continue
                if not visited[neighbor]:
                    dfs(neighbor, visited)

        visited = [False] * V
        dfs(c, visited)

        # Step 3: If d is still reachable, it's not a bridge
        return not visited[d]
