class Solution:
    def isCycle(self, V, edges):
        from collections import defaultdict

        # Step 1: Create adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Step 2: Initialize visited array
        visited = [False] * V

        # Step 3: DFS function
        def dfs(node, parent):
            visited[node] = True
            for neighbor in adj[node]:
                if not visited[neighbor]:  # Visit unvisited neighbor
                    if dfs(neighbor, node):
                        return True
                elif neighbor != parent:  # If visited and not parent, cycle exists
                    return True
            return False

        # Step 4: Check for cycle in each component
        for i in range(V):
            if not visited[i]:  # Only start DFS from unvisited nodes
                if dfs(i, -1):  # -1 as the parent of the first node
                    return True

        return False
