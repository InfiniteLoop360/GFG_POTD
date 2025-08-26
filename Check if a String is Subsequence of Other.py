class Solution:
    def isSubSeq(self, s1, s2):
        i = 0  # Pointer for s1
        j = 0  # Pointer for s2
        
        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                i += 1
            j += 1
        
        # If we have traversed the entire s1, it's a subsequence
        return i == len(s1)
