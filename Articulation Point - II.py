class Solution:
    def articulationPoints(self, V, edges):
        from collections import defaultdict

        def dfs(u, parent):
            nonlocal time
            visited[u] = True
            disc[u] = low[u] = time
            time += 1
            children = 0

            for v in graph[u]:
                if not visited[v]:
                    children += 1
                    dfs(v, u)
                    low[u] = min(low[u], low[v])

                    if parent != -1 and low[v] >= disc[u]:
                        ap[u] = True
                elif v != parent:
                    low[u] = min(low[u], disc[v])

            if parent == -1 and children > 1:
                ap[u] = True

        # Step 1: Build the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * V
        disc = [float('inf')] * V
        low = [float('inf')] * V
        ap = [False] * V  # articulation point flag for each vertex
        time = 0

        # Step 2: Run DFS on each unvisited component
        for i in range(V):
            if not visited[i]:
                dfs(i, -1)

        # Step 3: Collect articulation points
        result = [i for i, is_ap in enumerate(ap) if is_ap]
        return result if result else [-1]
