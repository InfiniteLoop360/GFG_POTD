class Solution:
    def maxLen(self, arr):
        # Replace 0s with -1s to use the prefix sum method
        for i in range(len(arr)):
            if arr[i] == 0:
                arr[i] = -1

        # Dictionary to store the first occurrence of each prefix sum
        prefix_sum_map = {}
        prefix_sum = 0
        max_length = 0

        for i in range(len(arr)):
            prefix_sum += arr[i]

            # If prefix sum is 0, the subarray from 0 to i has equal 0s and 1s
            if prefix_sum == 0:
                max_length = i + 1

            # If prefix_sum was seen before, calculate the length of the subarray
            if prefix_sum in prefix_sum_map:
                max_length = max(max_length, i - prefix_sum_map[prefix_sum])
            else:
                # Store the first occurrence of the prefix sum
                prefix_sum_map[prefix_sum] = i

        return max_length
