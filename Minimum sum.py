class Solution:
    def minSum(self, arr):
        arr.sort()
        num1 = []
        num2 = []

        for i in range(len(arr)):
            if i % 2 == 0:
                num1.append(str(arr[i]))
            else:
                num2.append(str(arr[i]))

        # Add num1 and num2 as strings without converting to int
        def addStrings(s1, s2):
            i, j = len(s1) - 1, len(s2) - 1
            carry = 0
            result = []

            while i >= 0 or j >= 0 or carry:
                digit1 = int(s1[i]) if i >= 0 else 0
                digit2 = int(s2[j]) if j >= 0 else 0
                total = digit1 + digit2 + carry
                result.append(str(total % 10))
                carry = total // 10
                i -= 1
                j -= 1

            return ''.join(result[::-1]).lstrip('0') or '0'

        s1 = ''.join(num1)
        s2 = ''.join(num2)
        return addStrings(s1, s2)
