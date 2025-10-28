from collections import deque

class Solution:
    def nearest(self, grid):
        n = len(grid)
        m = len(grid[0])
        
        # Distance matrix
        dist = [[-1 for _ in range(m)] for _ in range(n)]
        q = deque()
        
        # Step 1: Push all 1s into queue (multi-source BFS)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))
        
        # Directions for up, down, left, right
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        
        # Step 2: BFS traversal
        while q:
            i, j = q.popleft()
            
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                
                if 0 <= ni < n and 0 <= nj < m and dist[ni][nj] == -1:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))
        
        return dist
