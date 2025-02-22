class Solution:
    def maxLength(self, s):
        stack = [-1]  # Initialize stack with -1 as a base
        max_length = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # Store index of '('
            else:
                stack.pop()  # Try to match ')'
                if stack:
                    max_length = max(max_length, i - stack[-1])
                else:
                    stack.append(i)  # Store ')' as boundary
        
        return max_length
