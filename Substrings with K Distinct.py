class Solution:
    def countSubstr(self, s, k):
        return self.countAtMostKDistinct(s, k) - self.countAtMostKDistinct(s, k - 1)

    def countAtMostKDistinct(self, s, k):
        n = len(s)
        count = {}
        left = 0
        res = 0
        
        for right in range(n):
            count[s[right]] = count.get(s[right], 0) + 1
            
            while len(count) > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
            
            res += right - left + 1
        
        return res
