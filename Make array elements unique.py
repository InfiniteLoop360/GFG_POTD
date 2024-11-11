class Solution:
    def minIncrements(self, arr):
        # Step 1: Sort the array
        arr.sort()
        increments = 0
        
        # Step 2: Iterate through the array and ensure each element is unique
        for i in range(1, len(arr)):
            if arr[i] <= arr[i - 1]:  # If current element is not greater than the previous
                # Calculate the number of increments needed to make arr[i] unique
                needed_increment = arr[i - 1] + 1 - arr[i]
                arr[i] = arr[i - 1] + 1  # Make arr[i] unique
                increments += needed_increment  # Add the increments to the count
        
        return increments
