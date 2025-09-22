class Solution:
    def maxOfMins(self, arr):
        n = len(arr)
        
        # Step 1: Previous Smaller Element (PSE)
        pse = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            pse[i] = stack[-1] if stack else -1
            stack.append(i)
        
        # Step 2: Next Smaller Element (NSE)
        nse = [n] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            nse[i] = stack[-1] if stack else n
            stack.append(i)
        
        # Step 3: Fill result array
        res = [0] * (n+1)
        for i in range(n):
            length = nse[i] - pse[i] - 1
            res[length] = max(res[length], arr[i])
        
        # Step 4: Propagate results backwards
        for i in range(n-1, 0, -1):
            res[i] = max(res[i], res[i+1])
        
        return res[1:]
