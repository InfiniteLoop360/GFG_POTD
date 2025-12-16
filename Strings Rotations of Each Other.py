class Solution:
    def areRotations(self, s1, s2):
        # If lengths are not equal, cannot be rotations
        if len(s1) != len(s2):
            return False
        
        # Check if s2 is a substring of s1 concatenated with itself
        return s2 in (s1 + s1)
