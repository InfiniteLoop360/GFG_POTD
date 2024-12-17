class Solution:
    def aggressiveCows(self, stalls, k):
        def canPlaceCows(distance):
            count = 1  # Place the first cow
            last_position = stalls[0]
            
            for i in range(1, len(stalls)):
                if stalls[i] - last_position >= distance:
                    count += 1
                    last_position = stalls[i]
                    if count == k:
                        return True
            return False
        
        # Sort the stalls to place cows in increasing order
        stalls.sort()
        
        # Binary search on the answer
        low = 1
        high = stalls[-1] - stalls[0]
        best_distance = 0
        
        while low <= high:
            mid = (low + high) // 2
            if canPlaceCows(mid):
                best_distance = mid
                low = mid + 1  # Try for a larger minimum distance
            else:
                high = mid - 1  # Reduce the distance and try
        
        return best_distance
