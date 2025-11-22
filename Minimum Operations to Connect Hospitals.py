class Solution:
    def minConnect(self, V, edges):
        parent = list(range(V))
        rank = [0] * V
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False  # redundant (cycle)
            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[py] = px
                rank[px] += 1
            return True
        
        redundant = 0
        
        # Try to union all edges
        for u, v in edges:
            if not union(u, v):
                redundant += 1
        
        # Count number of connected components
        components = len({find(i) for i in range(V)})
        
        needed = components - 1
        
        # If we don’t have enough redundant edges → impossible
        if redundant < needed:
            return -1
        
        return needed
