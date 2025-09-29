from collections import deque

class Solution:
    def maxSubarrSum(self, arr, a, b):
        n = len(arr)
        prefix = [0] * (n + 1)
        
        # build prefix sums
        for i in range(n):
            prefix[i+1] = prefix[i] + arr[i]
        
        dq = deque()
        max_sum = float('-inf')
        
        for r in range(a-1, n):  # subarray ends at r
            # add index (r - a + 1) into deque (new left boundary possibility)
            new_l = r - a + 1
            while dq and prefix[dq[-1]] >= prefix[new_l]:
                dq.pop()
            dq.append(new_l)
            
            # remove indices out of range (too old for b constraint)
            while dq and dq[0] < r - b + 1:
                dq.popleft()
            
            # candidate sum = prefix[r+1] - prefix[min_l]
            max_sum = max(max_sum, prefix[r+1] - prefix[dq[0]])
        
        return max_sum
