class Solution:
    def longestSubarray(self, arr, k):
        # Dictionary to store the prefix sum and its first occurrence index
        prefix_sum_map = {}
        
        # Initialize variables
        prefix_sum = 0
        max_length = 0
        
        # Iterate through the array
        for i, num in enumerate(arr):
            # Update the prefix sum
            prefix_sum += num
            
            # Check if the current prefix sum is equal to k
            if prefix_sum == k:
                max_length = max(max_length, i + 1)

            # Check if (prefix_sum - k) is in the map
            if (prefix_sum - k) in prefix_sum_map:
                max_length = max(max_length, i - prefix_sum_map[prefix_sum - k])

            # Store the prefix sum and its index if not already present
            if prefix_sum not in prefix_sum_map:
                prefix_sum_map[prefix_sum] = i

        return max_length
