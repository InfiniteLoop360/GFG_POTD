class Solution:
    def checkRedundancy(self, s):
        stack = []
        operators = set(['+', '-', '*', '/'])
        
        for ch in s:
            if ch == ')':
                has_operator = False
                
                # Check inside the bracket
                while stack and stack[-1] != '(':
                    if stack[-1] in operators:
                        has_operator = True
                    stack.pop()
                
                # Pop '('
                stack.pop()
                
                # If no operator found, redundant bracket
                if not has_operator:
                    return True
            
            else:
                stack.append(ch)
        
        return False
