from collections import defaultdict

class Solution:
    def longestKSubstr(self, s, k):
        n = len(s)
        if n == 0 or k == 0:
            return -1
        
        char_freq = defaultdict(int)
        start = 0
        max_len = -1
        
        for end in range(n):
            char_freq[s[end]] += 1
            
            # Shrink window if unique characters exceed k
            while len(char_freq) > k:
                char_freq[s[start]] -= 1
                if char_freq[s[start]] == 0:
                    del char_freq[s[start]]
                start += 1

            # Update max_len when unique characters == k
            if len(char_freq) == k:
                max_len = max(max_len, end - start + 1)
        
        return max_len
