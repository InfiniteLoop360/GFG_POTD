class Solution:
    def maxSum(self, arr):
        max_score = 0
        n = len(arr)

        for i in range(n - 1):
            sum_two_smallest = arr[i] + arr[i + 1]
            max_score = max(max_score, sum_two_smallest)

        return max_score
