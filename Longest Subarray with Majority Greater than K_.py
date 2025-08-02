class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)
        # Transform array: +1 for > k, -1 for <= k
        transformed = [1 if x > k else -1 for x in arr]
        
        prefix_sum = 0
        max_len = 0
        first_occurrence = {0: -1}  # base case

        for i in range(n):
            prefix_sum += transformed[i]

            # If current prefix sum > 0, entire array from 0 to i is valid
            if prefix_sum > 0:
                max_len = i + 1
            else:
                # Check if prefix_sum - 1 has been seen before
                if (prefix_sum - 1) in first_occurrence:
                    length = i - first_occurrence[prefix_sum - 1]
                    max_len = max(max_len, length)

            # Store the first occurrence of this prefix sum
            if prefix_sum not in first_occurrence:
                first_occurrence[prefix_sum] = i

        return max_len
