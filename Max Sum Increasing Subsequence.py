class Solution:
    def maxSumIS(self, arr):
        n = len(arr)
        if n == 0:
            return 0

        # dp[i] = max sum of increasing subsequence ending at i
        dp = arr[:]  # start with single-element subsequence sum = arr[i]

        # optional: store predecessor to reconstruct subsequence
        prev = [-1] * n

        best = arr[0]
        best_idx = 0

        for i in range(n):
            for j in range(i):
                if arr[j] < arr[i]:
                    cand = dp[j] + arr[i]
                    if cand > dp[i]:
                        dp[i] = cand
                        prev[i] = j
            # update global best
            if dp[i] > best:
                best = dp[i]
                best_idx = i

        return best

    # If you also want the actual subsequence (not required by problem):
    def maxSumIS_with_sequence(self, arr):
        n = len(arr)
        if n == 0:
            return 0, []

        dp = arr[:]
        prev = [-1] * n

        best = arr[0]
        best_idx = 0

        for i in range(n):
            for j in range(i):
                if arr[j] < arr[i]:
                    cand = dp[j] + arr[i]
                    if cand > dp[i]:
                        dp[i] = cand
                        prev[i] = j
            if dp[i] > best:
                best = dp[i]
                best_idx = i

        # reconstruct subsequence
        seq = []
        idx = best_idx
        while idx != -1:
            seq.append(arr[idx])
            idx = prev[idx]
        seq.reverse()
        return best, seq
