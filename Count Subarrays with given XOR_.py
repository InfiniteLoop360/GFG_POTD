class Solution:
    def subarrayXor(self, arr, k):
        prefix_xor = 0
        count = 0
        freq = {}
        
        for num in arr:
            prefix_xor ^= num
            
            # If prefix_xor itself equals k
            if prefix_xor == k:
                count += 1
            
            # Check if (prefix_xor ^ k) was seen before
            if (prefix_xor ^ k) in freq:
                count += freq[prefix_xor ^ k]
            
            # Store/update frequency of prefix_xor
            freq[prefix_xor] = freq.get(prefix_xor, 0) + 1
        
        return count
