class Solution:
    def isPalinSent(self, s):
        # Step 1: Normalize the string
        cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
        
        # Step 2: Check if palindrome
        return cleaned == cleaned[::-1]
