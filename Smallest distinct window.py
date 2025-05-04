class Solution:
    def findSubString(self, s):
        n = len(s)
        if n == 0:
            return 0

        total_distinct = len(set(s))  # Step 1: count of unique characters

        freq = {}
        start = 0
        min_len = n + 1
        count = 0  # count of distinct characters in current window

        for end in range(n):
            freq[s[end]] = freq.get(s[end], 0) + 1

            # count unique characters in the window
            if freq[s[end]] == 1:
                count += 1

            # shrink window from the left if it has all distinct characters
            while count == total_distinct:
                min_len = min(min_len, end - start + 1)

                # shrink from the left
                freq[s[start]] -= 1
                if freq[s[start]] == 0:
                    count -= 1
                start += 1

        return min_len
