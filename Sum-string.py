class Solution:
    def isSumString(self, s):
        n = len(s)

        # Helper to check if given substrings form a valid sum string
        def check(a, b, remaining):
            if (a.startswith('0') and len(a) > 1) or (b.startswith('0') and len(b) > 1):
                return False

            sum_str = str(int(a) + int(b))
            if not remaining.startswith(sum_str):
                return False

            if len(remaining) == len(sum_str):
                return True

            return check(b, sum_str, remaining[len(sum_str):])

        # Try all possible combinations of first and second number
        for i in range(1, n):
            for j in range(1, n - i):
                a = s[:i]
                b = s[i:i + j]
                rest = s[i + j:]
                if check(a, b, rest):
                    return True

        return False
