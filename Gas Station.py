class Solution:
    def startStation(self, gas, cost):
        total_gas = sum(gas)
        total_cost = sum(cost)
        
        # If total gas available is less than total cost required, journey is impossible
        if total_gas < total_cost:
            return -1
        
        start_index = 0
        current_balance = 0
        
        for i in range(len(gas)):
            current_balance += gas[i] - cost[i]
            
            # If balance becomes negative, reset starting station to i+1
            if current_balance < 0:
                start_index = i + 1
                current_balance = 0  
        
        return start_index
