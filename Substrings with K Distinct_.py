class Solution:
    def countSubstr(self, s, k):
        
        def atMost(k):
            if k < 0:
                return 0
            
            left = 0
            freq = {}
            distinct = 0
            count = 0
            
            for right in range(len(s)):
                if s[right] not in freq or freq[s[right]] == 0:
                    distinct += 1
                    freq[s[right]] = 0
                
                freq[s[right]] += 1
                
                while distinct > k:
                    freq[s[left]] -= 1
                    if freq[s[left]] == 0:
                        distinct -= 1
                    left += 1
                
                count += (right - left + 1)
            
            return count
        
        return atMost(k) - atMost(k - 1)
