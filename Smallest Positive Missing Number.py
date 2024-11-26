class Solution:
    # Function to find the smallest positive number missing from the array.
    def missingNumber(self, arr):
        n = len(arr)
        
        # Step 1: Separate positive numbers from non-positive numbers
        # and move all positive numbers to the front of the array.
        j = 0
        for i in range(n):
            if arr[i] <= 0:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
        
        # Now the array is partitioned: [non-positive numbers | positive numbers]
        # Positive numbers start from index `j`.
        
        # Step 2: Mark presence of positive numbers using indexing
        for i in range(j, n):
            val = abs(arr[i])
            if val - 1 < n - j and arr[val - 1 + j] > 0:
                arr[val - 1 + j] = -arr[val - 1 + j]
        
        # Step 3: Find the first positive index in the positive part
        for i in range(j, n):
            if arr[i] > 0:
                return i - j + 1
        
        # If all indices are marked, return next number
        return n - j + 1
