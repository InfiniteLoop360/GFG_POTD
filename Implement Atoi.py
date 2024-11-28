class Solution:
    def myAtoi(self, s):
        # Constants for INT_MIN and INT_MAX
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # Step 1: Skip leading whitespaces
        i, n = 0, len(s)
        while i < n and s[i] == ' ':
            i += 1
        
        # Step 2: Handle the sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        # Step 3: Read digits and form the number
        num = 0
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        
        # Step 4: Apply sign
        num *= sign

        # Step 5: Clamp to INT_MIN and INT_MAX
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        
        return num
