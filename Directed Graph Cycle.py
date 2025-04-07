class Solution:
    def isCycle(self, V, edges):
        from collections import defaultdict

        # Step 1: Build adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)

        visited = [False] * V
        recStack = [False] * V

        def dfs(node):
            visited[node] = True
            recStack[node] = True

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
                elif recStack[neighbor]:  # Cycle detected
                    return True

            recStack[node] = False  # backtrack
            return False

        for i in range(V):
            if not visited[i]:
                if dfs(i):
                    return True
        return False
