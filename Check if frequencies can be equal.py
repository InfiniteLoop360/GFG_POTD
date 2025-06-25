from collections import Counter

class Solution:
    def sameFreq(self, s: str) -> bool:
        freq = Counter(s)
        freq_vals = list(freq.values())
        freq_counter = Counter(freq_vals)

        if len(freq_counter) == 1:
            # All frequencies are already the same
            return True

        if len(freq_counter) == 2:
            keys = list(freq_counter.keys())
            val1, val2 = keys[0], keys[1]

            # Case 1: one character occurs only once
            if (freq_counter[val1] == 1 and (val1 - 1 == val2 or val1 == 1)):
                return True
            if (freq_counter[val2] == 1 and (val2 - 1 == val1 or val2 == 1)):
                return True

        return False
