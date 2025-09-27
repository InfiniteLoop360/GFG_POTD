from collections import deque

class Solution:
    def kBitFlips(self, arr, k):
        n = len(arr)
        flips = 0         # total flips
        flip = 0          # current flip parity
        isFlipped = [0]*n # track where flips start
        
        for i in range(n):
            # If we moved past a flip window, remove its effect
            if i >= k:
                flip ^= isFlipped[i-k]
            
            # If current bit (after flip effect) is 0, we must flip here
            if arr[i] ^ flip == 0:
                if i + k > n:   # cannot flip (out of bounds)
                    return -1
                flips += 1
                flip ^= 1       # start new flip effect
                isFlipped[i] = 1
        
        return flips
