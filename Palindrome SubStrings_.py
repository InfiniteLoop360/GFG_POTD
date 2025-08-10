class Solution:
    def countPS(self, s):
        # Transform string
        T = "^#" + "#".join(s) + "#$"
        n = len(T)
        P = [0] * n
        center = right = 0
        
        for i in range(1, n - 1):
            mirror = 2 * center - i  # mirrored index of i
            
            if i < right:
                P[i] = min(right - i, P[mirror])
            
            # Expand
            while T[i + P[i] + 1] == T[i - P[i] - 1]:
                P[i] += 1
            
            # Update center/right if expanded past right
            if i + P[i] > right:
                center = i
                right = i + P[i]
        
        # Count substrings of length >= 2 in original string
        count = 0
        for radius in P:
            # radius in transformed string corresponds to original substrings
            # Every radius k means k//2 palindromes in original string
            if radius >= 2:
                count += (radius // 2)
        
        return count
