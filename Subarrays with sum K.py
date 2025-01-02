class Solution:
    def countSubarrays(self, arr, k):
        # Dictionary to store prefix sums and their frequencies
        prefix_sum_count = {}
        prefix_sum = 0
        count = 0

        # Iterate through the array
        for num in arr:
            # Update the prefix sum
            prefix_sum += num

            # Check if prefix_sum itself is equal to k
            if prefix_sum == k:
                count += 1

            # Check if (prefix_sum - k) exists in the dictionary
            if (prefix_sum - k) in prefix_sum_count:
                count += prefix_sum_count[prefix_sum - k]

            # Update the dictionary with the current prefix_sum
            if prefix_sum in prefix_sum_count:
                prefix_sum_count[prefix_sum] += 1
            else:
                prefix_sum_count[prefix_sum] = 1

        return count
