class Solution:
    def maxRemove(self, stones):
        # DSU Implementation
        parent = {}
        rank = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            pa = find(a)
            pb = find(b)
            if pa != pb:
                if rank[pa] < rank[pb]:
                    parent[pa] = pb
                elif rank[pb] < rank[pa]:
                    parent[pb] = pa
                else:
                    parent[pb] = pa
                    rank[pa] += 1
        
        OFFSET = 10001  # to separate rows and columns
        
        # Initialize parents
        for x, y in stones:
            row = x
            col = y + OFFSET
            
            if row not in parent:
                parent[row] = row
                rank[row] = 0
            if col not in parent:
                parent[col] = col
                rank[col] = 0
            
            union(row, col)
        
        # Count unique parents among nodes used
        unique_parents = set()
        for node in parent:
            unique_parents.add(find(node))
        
        # Max stones removed = total stones - connected components
        return len(stones) - len(unique_parents)
