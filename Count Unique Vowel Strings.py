from math import factorial
from collections import Counter

class Solution:
    def vowelCount(self, s):
        vowels = 'aeiou'
        freq = Counter(ch for ch in s if ch in vowels)
        
        if not freq:
            return 0

        m = len(freq)  # number of unique vowels
        perm = factorial(m)

        total = perm
        for count in freq.values():
            total *= count

        return total
