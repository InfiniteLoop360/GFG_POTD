class Solution:
    def getMaxArea(self, arr):
        stack = []  # Stack to store indices
        max_area = 0  # Variable to store the maximum area
        n = len(arr)  # Length of histogram array

        for i in range(n + 1):  # Iterate over all bars + 1 (to handle remaining stack elements)
            while stack and (i == n or arr[stack[-1]] > arr[i]):  
                height = arr[stack.pop()]  # Height of the popped bar
                width = i if not stack else i - stack[-1] - 1  # Calculate width
                max_area = max(max_area, height * width)  # Update max area
            
            stack.append(i)  # Push current index

        return max_area
