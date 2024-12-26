class Solution:
    def twoSum(self, arr, target):
        # Using a hash map to store elements and their indices
        seen = {}
        
        for i, num in enumerate(arr):
            complement = target - num
            
            # Check if the complement is in the map
            if complement in seen:
                return True  # Pair found
            
            # Store the current number and its index in the map
            seen[num] = i
        
        return False  # No pair found
