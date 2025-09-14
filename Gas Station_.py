class Solution:
    def startStation(self, gas, cost):
        n = len(gas)

        # Step 1: Feasibility check
        if sum(gas) < sum(cost):
            return -1

        # Step 2: Greedy traversal
        start = 0
        tank = 0
        for i in range(n):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0

        return start
