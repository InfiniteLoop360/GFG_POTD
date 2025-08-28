class Solution:
    def maxOnes(self, arr, k):
        left = 0
        max_len = 0
        zero_count = 0

        for right in range(len(arr)):
            # If we encounter a zero, increase zero_count
            if arr[right] == 0:
                zero_count += 1

            # If more than k zeros, shrink the window
            while zero_count > k:
                if arr[left] == 0:
                    zero_count -= 1
                left += 1

            # Update maximum length
            max_len = max(max_len, right - left + 1)

        return max_len
