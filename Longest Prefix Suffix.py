class Solution:
    def getLPSLength(self, s):
        n = len(s)
        lps = [0] * n  # Create LPS array of size n
        length = 0     # length of previous longest prefix suffix

        # Start from index 1 (index 0 is always 0)
        i = 1
        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps[-1]  # Last value is the answer
