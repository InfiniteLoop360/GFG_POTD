class Solution:
    def longestUniqueSubstr(self, s):
        # Dictionary to store the last index of each character
        last_index = {}
        max_length = 0
        start = 0  # Start index of the current substring

        for end in range(len(s)):
            # If the character is already in the substring, update the start index
            if s[end] in last_index and last_index[s[end]] >= start:
                start = last_index[s[end]] + 1
            
            # Update the last index of the current character
            last_index[s[end]] = end

            # Calculate the length of the current substring
            max_length = max(max_length, end - start + 1)

        return max_length
