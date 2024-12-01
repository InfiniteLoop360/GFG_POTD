class Solution:
    # Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self, s):
        # Step 1: Create a dictionary to store character counts
        char_count = {}
        
        # Step 2: Count occurrences of each character
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Step 3: Find the first character with a count of 1
        for char in s:
            if char_count[char] == 1:
                return char
        
        # Step 4: If no non-repeating character, return '$'
        return '$'
