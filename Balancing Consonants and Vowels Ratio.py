class Solution:
    def countBalanced(self, arr):
        from collections import defaultdict

        def count_vowels_and_consonants(word):
            vowels = set("aeiou")
            v = sum(1 for ch in word if ch in vowels)
            c = len(word) - v
            return v, c

        diff_map = defaultdict(int)
        diff_map[0] = 1  # initial state: diff = 0
        total_v, total_c = 0, 0
        count = 0

        for word in arr:
            v, c = count_vowels_and_consonants(word)
            total_v += v
            total_c += c
            diff = total_v - total_c
            count += diff_map[diff]
            diff_map[diff] += 1

        return count
