class Solution:
    def evaluate(self, arr):
        stack = []
        
        for token in arr:
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(int(a / b))  # Ensure truncation towards zero
            else:
                stack.append(int(token))  # Convert string to integer

        return stack[0]  # Final result
