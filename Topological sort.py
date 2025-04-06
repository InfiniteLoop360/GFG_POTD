from collections import deque, defaultdict

class Solution:
    def topoSort(self, V, edges):
        adj = defaultdict(list)
        indegree = [0] * V
        
        # Build adjacency list and compute in-degrees
        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1

        queue = deque()
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
        
        topo_order = []
        
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return topo_order if len(topo_order) == V else []
