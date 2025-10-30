from collections import deque

class Solution:
    def fill(self, grid):
        """
        Replace all 'O's that are surrounded by 'X' with 'X'.
        grid: list[list[str]] (characters 'O' or 'X')
        Returns the modified grid.
        """
        if not grid or not grid[0]:
            return grid

        n = len(grid)
        m = len(grid[0])
        q = deque()

        # Step 1: enqueue all border 'O's and mark them as safe with 'B'
        for j in range(m):
            if grid[0][j] == 'O':
                grid[0][j] = 'B'
                q.append((0, j))
            if grid[n-1][j] == 'O':
                grid[n-1][j] = 'B'
                q.append((n-1, j))

        for i in range(n):
            if grid[i][0] == 'O':
                grid[i][0] = 'B'
                q.append((i, 0))
            if grid[i][m-1] == 'O':
                grid[i][m-1] = 'B'
                q.append((i, m-1))

        # BFS from border O's
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 'O':
                    grid[nr][nc] = 'B'
                    q.append((nr, nc))

        # Step 3: flip enclosed 'O' -> 'X', restore 'B' -> 'O'
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'O':
                    grid[i][j] = 'X'
                elif grid[i][j] == 'B':
                    grid[i][j] = 'O'

        return grid
