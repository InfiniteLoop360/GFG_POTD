from collections import deque

class Solution:
    def longestSubarray(self, arr, x):
        min_dq, max_dq = deque(), deque()
        s = e = 0
        ans_start = ans_end = 0
        n = len(arr)
        
        while e < n:
            # Maintain min deque
            while min_dq and arr[min_dq[-1]] > arr[e]:
                min_dq.pop()
            # Maintain max deque
            while max_dq and arr[max_dq[-1]] < arr[e]:
                max_dq.pop()

            min_dq.append(e)
            max_dq.append(e)

            # Shrink window if condition is violated
            while arr[max_dq[0]] - arr[min_dq[0]] > x:
                if s == max_dq[0]:
                    max_dq.popleft()
                if s == min_dq[0]:
                    min_dq.popleft()
                s += 1

            # Update answer
            if e - s > ans_end - ans_start:
                ans_start, ans_end = s, e

            e += 1
        
        return arr[ans_start:ans_end+1]
