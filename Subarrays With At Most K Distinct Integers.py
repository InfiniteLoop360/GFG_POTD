from collections import defaultdict

class Solution:
    def countAtMostK(self, arr, k):
        if k == 0:
            return 0

        n = len(arr)
        count = defaultdict(int)
        left = 0
        res = 0
        distinct = 0

        for right in range(n):
            if count[arr[right]] == 0:
                distinct += 1
            count[arr[right]] += 1

            while distinct > k:
                count[arr[left]] -= 1
                if count[arr[left]] == 0:
                    distinct -= 1
                left += 1

            # Number of subarrays ending at 'right' with at most k distinct
            res += right - left + 1

        return res
