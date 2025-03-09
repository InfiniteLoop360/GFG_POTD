class Solution:
    def countPS(self, s):
        def expand_around_center(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 >= 2:  # Only count substrings of length >= 2
                    count += 1
                left -= 1
                right += 1
            return count

        total_palindromes = 0
        for i in range(len(s)):
            total_palindromes += expand_around_center(i, i)      # Odd-length palindromes
            total_palindromes += expand_around_center(i, i + 1)  # Even-length palindromes
        
        return total_palindromes
