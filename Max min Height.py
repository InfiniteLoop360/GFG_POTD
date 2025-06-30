class Solution():
    def maxMinHeight(self, arr, k, w):
        n = len(arr)

        def is_possible(target):
            diff = [0] * (n + 1)
            added = 0
            ops = 0
            for i in range(n):
                added += diff[i]
                curr_height = arr[i] + added
                if curr_height < target:
                    inc = target - curr_height
                    ops += inc
                    if ops > k:
                        return False
                    added += inc
                    if i + w < len(diff):
                        diff[i + w] -= inc
            return True

        low = min(arr)
        high = max(arr) + k
        ans = low

        while low <= high:
            mid = (low + high) // 2
            if is_possible(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
