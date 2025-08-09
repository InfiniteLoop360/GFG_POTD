class Solution:
    def z_function(self, s: str) -> list[int]:
        n = len(s)
        z = [0] * n
        l, r = 0, 0
        
        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            
            if i + z[i] - 1 > r:
                l = i
                r = i + z[i] - 1
        
        return z

    def getLongestPrefix(self, s: str) -> int:
        n = len(s)
        z = self.z_function(s)
        
        for i in range(n - 1, 0, -1):
            if z[i] == n - i:
                return i
        return -1
