class Solution:
    def countValid(self, n, arr):
        from itertools import product

        all_digits = set(range(10))
        allowed = set(arr)
        forbidden = all_digits - allowed

        if not forbidden:
            # All digits allowed, so every number is valid
            return 9 * (10 ** (n - 1))

        forbidden = list(forbidden)
        non_zero_forbidden = [d for d in forbidden if d != 0]

        # Total n-digit numbers
        total = 9 * (10 ** (n - 1))

        # If no valid starting digit in forbidden, can't form any n-digit number
        if not non_zero_forbidden:
            return total  # All numbers contain at least one allowed digit

        # Count how many n-digit numbers can be formed using only forbidden digits
        forbidden_count = len(non_zero_forbidden) * (len(forbidden) ** (n - 1))

        return total - forbidden_count
