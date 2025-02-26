class Solution:
    def maxOfMins(self, arr):
        n = len(arr)
        left = [-1] * n  
        right = [n] * n  
        stack = []
        
        # Compute Previous Smaller Element (PSE)
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        # Compute Next Smaller Element (NSE)
        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        # Compute the result array
        res = [0] * (n + 1)
        for i in range(n):
            window_size = right[i] - left[i] - 1
            res[window_size] = max(res[window_size], arr[i])

        # Fill unfilled entries in the result array
        for i in range(n - 1, 0, -1):
            res[i] = max(res[i], res[i + 1])

        return res[1:]
