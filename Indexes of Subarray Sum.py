class Solution:
    def subarraySum(self, arr, target):
        # Initialize variables
        left, current_sum = 0, 0

        # Iterate through the array
        for right in range(len(arr)):
            current_sum += arr[right]

            # Shrink the window if the sum exceeds the target
            while current_sum > target and left <= right:
                current_sum -= arr[left]
                left += 1

            # Check if we found the target sum
            if current_sum == target:
                return [left + 1, right + 1]  # Return 1-based indices

        # If no subarray is found, return -1
        return [-1]
