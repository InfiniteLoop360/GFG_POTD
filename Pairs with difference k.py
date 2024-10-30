from collections import Counter

class Solution:
    def countPairsWithDiffK(self, arr, k):
        freq = Counter(arr)
        count = 0
        
        for num in freq:
            # If num + k exists, then num and num + k form a valid pair
            if num + k in freq:
                count += freq[num] * freq[num + k]
                
        return count
