from collections import deque

class Solution:
    def longestSubarray(self, arr, x):
        n = len(arr)
        minDeque = deque()
        maxDeque = deque()
        
        left = 0
        best_len = 0
        best_start = 0
        
        for right in range(n):
            # Maintain minDeque (increasing order)
            while minDeque and arr[minDeque[-1]] > arr[right]:
                minDeque.pop()
            minDeque.append(right)
            
            # Maintain maxDeque (decreasing order)
            while maxDeque and arr[maxDeque[-1]] < arr[right]:
                maxDeque.pop()
            maxDeque.append(right)
            
            # Shrink window if condition violated
            while arr[maxDeque[0]] - arr[minDeque[0]] > x:
                left += 1
                if minDeque[0] < left:
                    minDeque.popleft()
                if maxDeque[0] < left:
                    maxDeque.popleft()
            
            # Update best window
            if right - left + 1 > best_len:
                best_len = right - left + 1
                best_start = left
        
        return arr[best_start: best_start + best_len]
