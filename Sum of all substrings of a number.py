class Solution:
    def sumSubstrings(self, s):
        n = len(s)
        total_sum = int(s[0])
        prev_sum = int(s[0])
        
        for i in range(1, n):
            num = int(s[i])
            # Contribution of s[i] to all substrings ending at i
            prev_sum = prev_sum * 10 + num * (i + 1)
            total_sum += prev_sum

        return total_sum
