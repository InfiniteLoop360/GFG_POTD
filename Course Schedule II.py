from collections import deque

class Solution:
    def findOrder(self, n, prerequisites):
        # Create adjacency list and in-degree count
        graph = [[] for _ in range(n)]
        indegree = [0] * n

        # Build the graph
        for x, y in prerequisites:
            graph[y].append(x)
            indegree[x] += 1

        # Queue for nodes with no prerequisites
        queue = deque()

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        order = []

        # BFS for topological sorting
        while queue:
            course = queue.popleft()
            order.append(course)

            for nxt in graph[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        # If all courses are included in result
        if len(order) == n:
            return order
        
        return []  # Return empty list if cycle exists
