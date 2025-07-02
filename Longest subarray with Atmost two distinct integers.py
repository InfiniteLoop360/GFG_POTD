from collections import defaultdict

class Solution:
    def totalElements(self, arr):
        freq = defaultdict(int)
        start = 0
        max_len = 0
        
        for end in range(len(arr)):
            freq[arr[end]] += 1
            
            # Shrink the window if more than 2 distinct elements
            while len(freq) > 2:
                freq[arr[start]] -= 1
                if freq[arr[start]] == 0:
                    del freq[arr[start]]
                start += 1
            
            # Update max length
            max_len = max(max_len, end - start + 1)
        
        return max_len
