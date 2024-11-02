class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        # Create a set to store the last k elements
        seen = set()
        
        # Iterate through the array
        for i in range(len(arr)):
            # If the element is already in the set, we found a duplicate within k distance
            if arr[i] in seen:
                return True
            
            # Add the current element to the set
            seen.add(arr[i])
            
            # If the set size is greater than k, remove the oldest element (i - k)
            if i >= k:
                seen.remove(arr[i - k])
        
        # No duplicates within k distance were found
        return False
