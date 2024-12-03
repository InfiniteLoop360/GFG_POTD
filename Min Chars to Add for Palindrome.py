class Solution:
    def minChar(self, s):
        # Reverse the string
        rev_s = s[::-1]
        
        # Create a new string with a separator
        new_str = s + "#" + rev_s
        
        # KMP LPS array
        n = len(new_str)
        lps = [0] * n
        
        # Compute the LPS array
        j = 0
        for i in range(1, n):
            while (j > 0 and new_str[i] != new_str[j]):
                j = lps[j - 1]
            
            if new_str[i] == new_str[j]:
                j += 1
                lps[i] = j
        
        # The length of the longest prefix which is also a suffix
        longest_palindrome_suffix_length = lps[n - 1]
        
        # The result is the number of characters we need to add to the front
        return len(s) - longest_palindrome_suffix_length
