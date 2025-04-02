from collections import deque

class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        V = len(adj)  # Number of vertices
        visited = set()  # Set to keep track of visited nodes
        queue = deque([0])  # BFS queue initialized with the starting node (0)
        bfs_order = []  # List to store BFS traversal order

        while queue:
            node = queue.popleft()  # Remove and process the first element
            if node not in visited:
                visited.add(node)  # Mark node as visited
                bfs_order.append(node)  # Add to result
                
                for neighbor in adj[node]:  # Traverse all adjacent nodes
                    if neighbor not in visited:
                        queue.append(neighbor)  # Add unvisited neighbors to queue
        
        return bfs_order
