import math

class Solution:
    def smallestDivisor(self, arr, k):
        def get_sum(divisor):
            return sum((x + divisor - 1) // divisor for x in arr)

        low, high = 1, max(arr)
        answer = high

        while low <= high:
            mid = (low + high) // 2
            if get_sum(mid) <= k:
                answer = mid
                high = mid - 1
            else:
                low = mid + 1

        return answer
