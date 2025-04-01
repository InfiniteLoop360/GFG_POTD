class Solution:
    
    # Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        visited = set()  # To track visited nodes
        traversal = []   # Stores DFS traversal result
        
        def dfs_helper(node):
            if node in visited:
                return
            visited.add(node)
            traversal.append(node)
            for neighbor in adj[node]:  # Visit neighbors in given order
                dfs_helper(neighbor)
        
        dfs_helper(0)  # Start DFS from vertex 0
        return traversal
