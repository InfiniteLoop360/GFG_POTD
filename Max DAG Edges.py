class Solution:
    def maxEdgesToAdd(self, V, edges):
        from collections import deque
        
        # Adjacency list and indegree tracking
        adj = [[] for _ in range(V)]
        indegree = [0] * V
        
        # Boolean matrix to mark existing edges
        exists = [[False] * V for _ in range(V)]
        
        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1
            exists[u][v] = True
        
        # Topological Sort (Kahn’s algorithm)
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        # Count missing valid edges (only forward in topological order)
        pos = [0] * V   # Map node → topo index for faster access
        for i, node in enumerate(topo):
            pos[node] = i
        
        count = 0
        for i in range(V):
            for j in range(i + 1, V):
                u = topo[i]
                v = topo[j]
                if not exists[u][v]:
                    count += 1
        
        return count
