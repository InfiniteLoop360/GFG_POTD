class Solution:
    # Function to find the sum of contiguous subarray with the maximum sum.
    def maxSubArraySum(self, arr):
        # Initialize variables for maximum sum and current sum
        max_sum = float('-inf')
        current_sum = 0
        
        # Traverse through the array
        for num in arr:
            # Update the current sum
            current_sum += num
            
            # Update max_sum if current_sum is greater
            max_sum = max(max_sum, current_sum)
            
            # Reset current_sum to 0 if it drops below 0
            if current_sum < 0:
                current_sum = 0
        
        return max_sum
