class Solution:
    def nextGreater(self, arr):
        n = len(arr)
        res = [-1] * n
        stack = []  # stack holds values in strictly decreasing order (top at end)

        # traverse from 2n-1 down to 0
        for i in range(2 * n - 1, -1, -1):
            val = arr[i % n]
            # remove all elements <= val, because they can't be next greater for earlier elements
            while stack and stack[-1] <= val:
                stack.pop()
            # record answer only for the first pass (i < n)
            if i < n:
                res[i] = stack[-1] if stack else -1
            # push current value as a candidate for elements to the left
            stack.append(val)

        return res
