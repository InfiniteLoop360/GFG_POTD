class Solution:
    def countAtMostK(self, arr, k):
        left = 0
        freq = {}
        distinct = 0
        ans = 0
        
        for right in range(len(arr)):
            if arr[right] not in freq or freq[arr[right]] == 0:
                distinct += 1
                freq[arr[right]] = 0
            
            freq[arr[right]] += 1
            
            while distinct > k:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    distinct -= 1
                left += 1
            
            ans += (right - left + 1)
        
        return ans
