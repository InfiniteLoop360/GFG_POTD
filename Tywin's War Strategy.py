import math

class Solution:
    def minSoldiers(self, arr, k):
        n = len(arr)
        target = math.ceil(n / 2)
        
        lucky_count = 0
        costs = []
        
        for soldiers in arr:
            if soldiers % k == 0:
                lucky_count += 1
            else:
                cost = k - (soldiers % k)
                costs.append(cost)
        
        # Already enough lucky troops
        if lucky_count >= target:
            return 0
        
        # Need to convert some troops
        need = target - lucky_count
        costs.sort()
        
        return sum(costs[:need])
