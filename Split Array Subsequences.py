from collections import Counter, defaultdict

class Solution:
    def isPossible(self, arr, k):
        count = Counter(arr)
        end_at = defaultdict(int)

        for num in arr:
            if count[num] == 0:
                continue

            # Case 1: extend existing subsequence
            if end_at[num - 1] > 0:
                end_at[num - 1] -= 1
                end_at[num] += 1
                count[num] -= 1

            # Case 2: start new subsequence of length k
            elif all(count[num + i] > 0 for i in range(k)):
                for i in range(k):
                    count[num + i] -= 1
                end_at[num + k - 1] += 1

            else:
                return False

        return True
