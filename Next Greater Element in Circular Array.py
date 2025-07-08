class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        result = [-1] * n
        stack = []

        # Traverse the array twice for circular effect
        for i in range(2 * n):
            while stack and arr[i % n] > arr[stack[-1]]:
                result[stack.pop()] = arr[i % n]
            if i < n:
                stack.append(i)
        
        return result
