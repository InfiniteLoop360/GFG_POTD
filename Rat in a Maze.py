class Solution:
    def ratInMaze(self, maze):
        """
        Return list of path strings from (0,0) to (n-1,n-1).
        Each path is a sequence of characters among 'D','L','R','U'.
        """
        n = len(maze)
        if n == 0:
            return []
        # If start or end blocked, no paths
        if maze[0][0] == 0 or maze[n-1][n-1] == 0:
            return []

        results = []
        # visited matrix
        visited = [[False]*n for _ in range(n)]

        # Directions: label -> (dr, dc)
        # We choose an order here; final output will be sorted anyway.
        dirs = [('D', 1, 0), ('L', 0, -1), ('R', 0, 1), ('U', -1, 0)]

        def valid(r, c):
            return 0 <= r < n and 0 <= c < n and maze[r][c] == 1 and not visited[r][c]

        def dfs(r, c, path):
            # If reached destination, record path
            if r == n-1 and c == n-1:
                results.append(path)
                return

            # Try all 4 directions
            for ch, dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if valid(nr, nc):
                    visited[nr][nc] = True
                    dfs(nr, nc, path + ch)
                    visited[nr][nc] = False

        # start DFS from (0,0)
        visited[0][0] = True
        dfs(0, 0, "")

        # Return sorted lexicographically (problem requires lexicographically smallest order)
        results.sort()
        return results
