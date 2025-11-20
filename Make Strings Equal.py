class Solution:
    def minCost(self, s, t, transform, cost):
        # Step 1: Initialize distance matrix
        INF = 10**18
        dist = [[INF]*26 for _ in range(26)]
        
        # Distance to itself is 0
        for i in range(26):
            dist[i][i] = 0
        
        # Insert the given transformations
        for i in range(len(transform)):
            u = ord(transform[i][0]) - ord('a')
            v = ord(transform[i][1]) - ord('a')
            dist[u][v] = min(dist[u][v], cost[i])
        
        # Step 2: Floyd Warshall for all-pairs shortest path
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Step 3: Calculate minimum cost to make s and t identical
        total_cost = 0
        
        for i in range(len(s)):
            a = ord(s[i]) - ord('a')
            b = ord(t[i]) - ord('a')
            
            best = INF
            for x in range(26):  # try to make both chars into x
                if dist[a][x] < INF and dist[b][x] < INF:
                    best = min(best, dist[a][x] + dist[b][x])
            
            if best == INF:
                return -1
            
            total_cost += best
        
        return total_cost
