class Solution:
    def search(self, pat, txt):
        # Step 1: Preprocess the pattern to create LPS array
        def computeLPSArray(pattern):
            n = len(pattern)
            lps = [0] * n
            length = 0  # length of the previous longest prefix suffix
            i = 1

            while i < n:
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps
        
        # Step 2: Search pattern in text using KMP
        m = len(pat)
        n = len(txt)
        
        # Preprocess pattern
        lps = computeLPSArray(pat)
        i = 0  # index for txt[]
        j = 0  # index for pat[]
        
        result = []
        
        while i < n:
            if pat[j] == txt[i]:
                i += 1
                j += 1
            
            if j == m:
                result.append(i - j)  # found a match, append the index
                j = lps[j - 1]  # Use LPS to avoid re-checking characters
            
            elif i < n and pat[j] != txt[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        
        return result
