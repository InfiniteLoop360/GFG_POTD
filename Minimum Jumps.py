class Solution:
    def minJumps(self, arr):
        n = len(arr)
        if n <= 1:
            return 0  # Already at the end
        if arr[0] == 0:
            return -1  # Cannot move from the start
        
        jumps = 0
        farthest = 0
        end = 0
        
        for i in range(n - 1):  # No need to check the last element
            farthest = max(farthest, i + arr[i])  # Update farthest reach
            
            if i == end:  # Time to jump
                jumps += 1
                end = farthest  # Set new range
                
                if end >= n - 1:  # Reached or crossed the last index
                    return jumps
        
        return -1  # If we never reach the last index
