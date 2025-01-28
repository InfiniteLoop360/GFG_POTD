from itertools import permutations

class Solution:
    def findPermutation(self, s):
        # Use a set to ensure unique permutations
        unique_permutations = set(permutations(s))
        # Convert each tuple to a string and return as a sorted list
        return sorted("".join(p) for p in unique_permutations)
