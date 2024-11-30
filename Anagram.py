class Solution:
    # Function to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        # If lengths are not equal, they can't be anagrams
        if len(s1) != len(s2):
            return False
        
        # Count the frequency of characters in both strings
        freq1 = {}
        freq2 = {}
        
        for char in s1:
            freq1[char] = freq1.get(char, 0) + 1
        
        for char in s2:
            freq2[char] = freq2.get(char, 0) + 1
        
        # Compare both frequency dictionaries
        return freq1 == freq2
