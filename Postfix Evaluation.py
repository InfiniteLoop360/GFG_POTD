class Solution:
    def evaluatePostfix(self, arr):
        """
        Evaluate a postfix (RPN) expression in arr and return integer result.
        Operators supported: +, -, *, / (floor division), ^ (power).
        It is guaranteed expression is valid and results fit in 32-bit signed int.
        """
        stack = []
        for token in arr:
            if token not in {"+", "-", "*", "/", "^"}:
                # operand
                stack.append(int(token))
            else:
                # operator: pop b then a (order matters)
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # floor division as required by problem statement
                    # Python's // already does floor division for negatives too.
                    # Note: division by zero should not happen given valid input.
                    stack.append(a // b)
                elif token == "^":
                    stack.append(a ** b)

        return stack[-1]
