class Solution:
    # Function to find the first equilibrium point in the array.
    def findEquilibrium(self, arr):
        total_sum = sum(arr)  # Total sum of the array
        left_sum = 0  # Initialize left sum to 0
        
        for i in range(len(arr)):
            # Right sum = total sum - left sum - current element
            right_sum = total_sum - left_sum - arr[i]
            
            # Check if left sum equals right sum
            if left_sum == right_sum:
                return i  # Return the index of the equilibrium point
            
            # Update left sum to include the current element
            left_sum += arr[i]
        
        return -1  # Return -1 if no equilibrium point is found
