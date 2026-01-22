class Solution:
    def subarrayRanges(self, arr):
        n = len(arr)

        def sumSubarrayMin(arr):
            stack = []
            left = [0] * n
            right = [0] * n

            # Previous smaller
            for i in range(n):
                while stack and arr[stack[-1]] > arr[i]:
                    stack.pop()
                left[i] = i - stack[-1] if stack else i + 1
                stack.append(i)

            stack.clear()

            # Next smaller or equal
            for i in range(n - 1, -1, -1):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                right[i] = stack[-1] - i if stack else n - i
                stack.append(i)

            total = 0
            for i in range(n):
                total += arr[i] * left[i] * right[i]
            return total

        def sumSubarrayMax(arr):
            stack = []
            left = [0] * n
            right = [0] * n

            # Previous greater
            for i in range(n):
                while stack and arr[stack[-1]] < arr[i]:
                    stack.pop()
                left[i] = i - stack[-1] if stack else i + 1
                stack.append(i)

            stack.clear()

            # Next greater or equal
            for i in range(n - 1, -1, -1):
                while stack and arr[stack[-1]] <= arr[i]:
                    stack.pop()
                right[i] = stack[-1] - i if stack else n - i
                stack.append(i)

            total = 0
            for i in range(n):
                total += arr[i] * left[i] * right[i]
            return total

        return sumSubarrayMax(arr) - sumSubarrayMin(arr)
