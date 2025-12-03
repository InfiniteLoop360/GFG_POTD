class Solution:
    def tsp(self, cost):
        n = len(cost)
        FULL = (1 << n)

        # dp[mask][i] = minimum cost to reach city i after visiting mask cities
        dp = [[float('inf')] * n for _ in range(FULL)]

        # Base Case: start at city 0 with only city 0 visited
        dp[1][0] = 0   # 0001 mask (only city 0 visited)

        for mask in range(FULL):
            for u in range(n):
                if not (mask & (1 << u)):
                    continue
                for v in range(n):
                    if mask & (1 << v):
                        continue
                    new_mask = mask | (1 << v)
                    dp[new_mask][v] = min(
                        dp[new_mask][v],
                        dp[mask][u] + cost[u][v]
                    )

        ans = float('inf')
        final_mask = FULL - 1
        for i in range(n):
            ans = min(ans, dp[final_mask][i] + cost[i][0])

        return ans
