from collections import deque

class Solution:
    def manacher_odd(self, s):
        """Returns array d1 where d1[i] is the radius of odd palindrome centered at i."""
        n = len(s)
        d1 = [0] * n
        l, r = 0, -1
        for i in range(n):
            k = 1 if i > r else min(d1[l + r - i], r - i + 1)
            while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
                k += 1
            d1[i] = k
            if i + k - 1 > r:
                l = i - k + 1
                r = i + k - 1
        return d1

    def compute_endLen(self, s, d1):
        """Computes the length of the longest odd palindrome ending at each position."""
        n = len(s)
        endLen = [0] * n
        R = [i + d1[i] - 1 for i in range(n)]
        q = deque()

        for p in range(n):
            q.append(p)
            while q and R[q[0]] < p:
                q.popleft()
            if q:
                endLen[p] = 2 * (p - q[0]) + 1
            else:
                endLen[p] = 0
        return endLen

    def maxSum(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0

        # Palindromes in original string
        d1 = self.manacher_odd(s)
        endLen = self.compute_endLen(s, d1)

        # Palindromes in reversed string
        rs = s[::-1]
        d1r = self.manacher_odd(rs)
        endLenR = self.compute_endLen(rs, d1r)

        # startLen[i] = length of longest odd palindrome starting at position i
        startLen = [0] * n
        for i in range(n):
            startLen[n - 1 - i] = endLenR[i]

        # Best prefix and suffix arrays
        bestPref = [0] * n
        bestPref[0] = endLen[0]
        for i in range(1, n):
            bestPref[i] = max(bestPref[i - 1], endLen[i])

        bestSuf = [0] * n
        bestSuf[-1] = startLen[-1]
        for i in range(n - 2, -1, -1):
            bestSuf[i] = max(bestSuf[i + 1], startLen[i])

        # Max sum of two disjoint palindromes
        ans = 0
        for i in range(n - 1):
            ans = max(ans, bestPref[i] + bestSuf[i + 1])

        return ans
