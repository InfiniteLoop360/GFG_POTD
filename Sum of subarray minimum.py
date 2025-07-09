class Solution:
    def sumSubMins(self, arr):
        MOD = 10**9 + 7
        n = len(arr)
        
        # Previous Less Element (PLE)
        ple = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            ple[i] = stack[-1] if stack else -1
            stack.append(i)

        # Next Less Element (NLE)
        nle = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            nle[i] = stack[-1] if stack else n
            stack.append(i)

        # Calculate the total sum
        result = 0
        for i in range(n):
            left = i - ple[i]
            right = nle[i] - i
            result = (result + arr[i] * left * right) % MOD

        return result
