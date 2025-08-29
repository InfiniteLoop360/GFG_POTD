from collections import Counter

class Solution:
    def smallestWindow(self, s, p):
        if not s or not p:
            return ""
        
        need = Counter(p)               # frequency of pattern
        window = {}                     # current window char counts
        required = len(need)            # number of unique chars required
        formed = 0                      # number of chars satisfied in window
        
        l, r = 0, 0
        min_len = float("inf")
        min_window = ""
        
        while r < len(s):
            # Expand right
            char = s[r]
            window[char] = window.get(char, 0) + 1
            
            if char in need and window[char] == need[char]:
                formed += 1
            
            # Try to shrink from left
            while l <= r and formed == required:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_window = s[l:r+1]
                
                # Pop from left
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    formed -= 1
                l += 1
            
            r += 1
        
        return min_window if min_len != float("inf") else ""
