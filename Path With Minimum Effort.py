import heapq

class Solution:
    def minCostPath(self, mat):
        n = len(mat)
        m = len(mat[0])

        # Dijkstra on grid
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0

        # Min-heap: (effort, x, y)
        pq = [(0, 0, 0)]

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while pq:
            effort, x, y = heapq.heappop(pq)

            # If we reached the destination
            if x == n-1 and y == m-1:
                return effort

            # If effort already larger than best known, skip
            if effort > dist[x][y]:
                continue

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m:
                    diff = abs(mat[x][y] - mat[nx][ny])
                    new_effort = max(effort, diff)

                    if new_effort < dist[nx][ny]:
                        dist[nx][ny] = new_effort
                        heapq.heappush(pq, (new_effort, nx, ny))

        # Should never reach here in valid input
        return dist[n-1][m-1]
