class Solution:
    def addBinary(self, s1, s2):
        # Initialize pointers for both strings
        i, j = len(s1) - 1, len(s2) - 1
        carry = 0  # Initialize carry to 0
        result = []  # To store the resulting binary string

        # Iterate as long as there are digits to process in either string or carry is not zero
        while i >= 0 or j >= 0 or carry:
            # Get the current digits (convert '0' or '1' to int or use 0 if index out of range)
            digit1 = int(s1[i]) if i >= 0 else 0
            digit2 = int(s2[j]) if j >= 0 else 0

            # Compute the sum of current digits and carry
            total = digit1 + digit2 + carry

            # Append the current bit (total % 2) to the result
            result.append(str(total % 2))

            # Update the carry (total // 2)
            carry = total // 2

            # Move to the next digits
            i -= 1
            j -= 1

        # Since we built the result in reverse order, reverse it back
        # Join the result and strip any leading zeros, but handle the case where the result is just 0
        return ''.join(reversed(result)).lstrip('0') or '0'
