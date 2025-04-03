from collections import deque

class Solution:
    def orangesRotting(self, mat):
        if not mat:
            return -1
        
        n, m = len(mat), len(mat[0])
        queue = deque()
        fresh_count = 0

        # Step 1: Store initial rotten oranges and count fresh ones
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 2:
                    queue.append((i, j, 0))  # (row, col, time)
                elif mat[i][j] == 1:
                    fresh_count += 1

        # If no fresh oranges exist, return 0 immediately
        if fresh_count == 0:
            return 0

        # Step 2: BFS traversal to rot fresh oranges
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        time_elapsed = 0

        while queue:
            r, c, time_elapsed = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] == 1:
                    mat[nr][nc] = 2  # Mark orange as rotten
                    fresh_count -= 1  # Reduce fresh count
                    queue.append((nr, nc, time_elapsed + 1))  # Push into queue

        # If any fresh orange is left, return -1
        return time_elapsed if fresh_count == 0 else -1
