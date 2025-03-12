class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        if n == 2:
            return min(cost[0], cost[1])

        prev2 = cost[0]  # Cost to reach the first step
        prev1 = cost[1]  # Cost to reach the second step

        for i in range(2, n):
            curr = cost[i] + min(prev1, prev2)  # Compute cost for current step
            prev2, prev1 = prev1, curr  # Update prev2 and prev1

        return min(prev1, prev2)  # Minimum cost to reach top
