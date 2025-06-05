class Solution:
    def countPaths(self, edges, V, src, dest):
        from collections import defaultdict
        import sys
        sys.setrecursionlimit(10**6)

        # Step 1: Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        # Step 2: DFS with memoization
        memo = {}

        def dfs(u):
            if u == dest:
                return 1
            if u in memo:
                return memo[u]
            
            total_paths = 0
            for neighbor in graph[u]:
                total_paths += dfs(neighbor)

            memo[u] = total_paths
            return total_paths

        return dfs(src)
