from collections import deque

class Solution:    
    def rotateDeque(self, dq, type, k):
        n = len(dq)
        if n == 0:
            return dq
        
        # Step 1: optimize k
        k = k % n
        
        # Step 2: rotate based on type
        if type == 1:  # right rotation
            dq.rotate(k)
        elif type == 2:  # left rotation
            dq.rotate(-k)
        
        return list(dq)   # returning as list (since test expects list)
