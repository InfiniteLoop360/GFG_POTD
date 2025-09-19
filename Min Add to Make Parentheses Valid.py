class Solution:
    def minParentheses(self, s):
        open_needed = 0   # count of '(' needed
        close_needed = 0  # count of ')' needed

        for ch in s:
            if ch == '(':
                close_needed += 1   # expect one more ')'
            else:  # ch == ')'
                if close_needed > 0:
                    close_needed -= 1  # match existing '('
                else:
                    open_needed += 1   # need an extra '('

        return open_needed + close_needed
