class Solution:
    def maxCircularSum(self, arr):
        def kadane(nums):
            max_current = max_global = nums[0]
            for num in nums[1:]:
                max_current = max(num, max_current + num)
                max_global = max(max_global, max_current)
            return max_global

        def min_kadane(nums):
            min_current = min_global = nums[0]
            for num in nums[1:]:
                min_current = min(num, min_current + num)
                min_global = min(min_global, min_current)
            return min_global

        total_sum = sum(arr)
        max_normal = kadane(arr)
        min_subarray_sum = min_kadane(arr)

        if max_normal < 0:
            return max_normal  # All elements are negative

        max_circular = total_sum - min_subarray_sum
        return max(max_normal, max_circular)
