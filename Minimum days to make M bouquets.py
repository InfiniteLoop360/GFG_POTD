class Solution:
    def minDaysBloom(self, arr, k, m):
        n = len(arr)
        if n < m * k:   # not enough flowers
            return -1
        
        low, high = min(arr), max(arr)
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if self.canMake(arr, mid, m, k):
                ans = mid
                high = mid - 1  # try smaller day
            else:
                low = mid + 1   # need more days
        
        return ans
    
    def canMake(self, arr, day, m, k):
        bouquets = 0
        flowers = 0
        
        for bloom in arr:
            if bloom <= day:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0
        
        return bouquets >= m
