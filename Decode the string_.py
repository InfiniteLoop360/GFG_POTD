class Solution:
    def decodedString(self, s):
        num_stack = []
        str_stack = []
        current_str = ""
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)   # build full number
            elif ch == '[':
                num_stack.append(num)
                str_stack.append(current_str)
                num = 0
                current_str = ""
            elif ch == ']':
                k = num_stack.pop()
                prev_str = str_stack.pop()
                current_str = prev_str + k * current_str
            else:
                current_str += ch

        return current_str
