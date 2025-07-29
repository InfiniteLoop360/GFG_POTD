class Solution:
    def asciirange(self, s):
        first = {}
        last = {}

        # Record first and last occurrence
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        result = []

        for ch in first:
            start = first[ch]
            end = last[ch]

            if start != end:
                # Sum ASCII values strictly between start and end
                ascii_sum = sum(ord(s[i]) for i in range(start + 1, end))
                if ascii_sum != 0:
                    result.append(ascii_sum)

        return result
