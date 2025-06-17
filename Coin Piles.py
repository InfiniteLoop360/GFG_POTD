from bisect import bisect_right

class Solution:
    def minimumCoins(self, arr, k):
        arr.sort()
        n = len(arr)

        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + arr[i]

        # Precompute suffix sum
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + arr[i]

        ans = float('inf')

        for i in range(n):
            base = arr[i]
            max_allowed = base + k
            # Find the first index greater than max_allowed
            j = bisect_right(arr, max_allowed)

            # Remove all left of i (entire piles)
            left_cost = prefix_sum[i]

            # Reduce all values after j to max_allowed
            count = n - j
            if count > 0:
                sum_over = suffix_sum[j]
                right_cost = sum_over - count * max_allowed
            else:
                right_cost = 0

            total_cost = left_cost + right_cost
            ans = min(ans, total_cost)

        return ans
