class Solution:
    def splitArray(self, arr, k):
        def is_possible(max_sum):
            count = 1
            curr_sum = 0
            for num in arr:
                if curr_sum + num > max_sum:
                    count += 1
                    curr_sum = num
                else:
                    curr_sum += num
            return count <= k

        low = max(arr)
        high = sum(arr)
        result = high

        while low <= high:
            mid = (low + high) // 2
            if is_possible(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result
