class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        stack = []
        result = [-1] * n  # Default to -1
        
        for i in range(n - 1, -1, -1):  # Traverse from right to left
            while stack and stack[-1] <= arr[i]:  
                stack.pop()  # Remove smaller elements
            
            if stack:
                result[i] = stack[-1]  # Top element is the NGE
            
            stack.append(arr[i])  # Push current element
        
        return result
