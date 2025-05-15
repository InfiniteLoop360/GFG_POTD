class Solution:
    def countSubstring(self, s: str) -> int:
        from collections import Counter

        freq = Counter(s)
        count = 0

        for ch in freq:
            f = freq[ch]
            count += (f * (f + 1)) // 2  # f single letters + fC2 substrings

        return count
