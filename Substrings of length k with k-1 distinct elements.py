from collections import defaultdict

class Solution:
    def substrCount(self, s, k):
        if len(s) < k:
            return 0
        
        freq = defaultdict(int)
        count = 0
        
        # Initialize first window
        for i in range(k):
            freq[s[i]] += 1
        
        if len(freq) == k - 1:
            count += 1
        
        # Slide the window
        for i in range(k, len(s)):
            # Remove leftmost character from window
            left_char = s[i - k]
            freq[left_char] -= 1
            if freq[left_char] == 0:
                del freq[left_char]
            
            # Add new character to window
            freq[s[i]] += 1
            
            if len(freq) == k - 1:
                count += 1
        
        return count
