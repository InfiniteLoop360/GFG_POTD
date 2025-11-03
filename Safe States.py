from collections import deque

class Solution:
    def safeNodes(self, V, edges):
        adj = [[] for _ in range(V)]
        outdegree = [0] * V
        
        # Build the reverse graph
        for u, v in edges:
            adj[v].append(u)
            outdegree[u] += 1
        
        q = deque()
        
        # Add terminal nodes
        for i in range(V):
            if outdegree[i] == 0:
                q.append(i)
        
        safe = [False] * V
        
        # Reverse BFS like Topological Sort
        while q:
            node = q.popleft()
            safe[node] = True
            
            for prev in adj[node]:
                outdegree[prev] -= 1
                if outdegree[prev] == 0:
                    q.append(prev)
        
        result = [i for i in range(V) if safe[i]]
        return result
