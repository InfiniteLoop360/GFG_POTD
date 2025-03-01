class Solution:
    def decodedString(self, s):
        stack = []
        num_stack = []
        curr_num = 0
        curr_str = ""
        
        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)  # Handle multi-digit numbers
            elif char == '[':
                num_stack.append(curr_num)
                stack.append(curr_str)
                curr_num = 0
                curr_str = ""
            elif char == ']':
                repeat_count = num_stack.pop()
                decoded_part = stack.pop() + curr_str * repeat_count
                curr_str = decoded_part
            else:
                curr_str += char
        
        return curr_str
