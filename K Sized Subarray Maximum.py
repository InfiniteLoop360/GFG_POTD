from collections import deque

class Solution:
    def maxOfSubarrays(self, arr, k):
        n = len(arr)
        result = []
        dq = deque()
        
        for i in range(n):
            # Remove elements out of the current window
            if dq and dq[0] == i - k:
                dq.popleft()

            # Remove elements smaller than current from the back
            while dq and arr[dq[-1]] < arr[i]:
                dq.pop()
                
            # Add the current element index
            dq.append(i)

            # Append max element for the current window (only after filling k elements)
            if i >= k - 1:
                result.append(arr[dq[0]])

        return result
