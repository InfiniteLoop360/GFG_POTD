class Solution:
    def calculateSpan(self, arr):
        n = len(arr)
        stack = []
        span = [0] * n  # Store span values

        for i in range(n):
            # Pop elements from stack while the stack is not empty 
            # and the top element is less than or equal to arr[i]
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()

            # If stack is empty, all previous elements are smaller
            if not stack:
                span[i] = i + 1  # Span = index + 1 (entire range)
            else:
                span[i] = i - stack[-1]  # Span = index difference

            stack.append(i)  # Push the current index

        return span
