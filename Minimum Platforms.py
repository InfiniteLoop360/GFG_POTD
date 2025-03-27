class Solution:
    def minimumPlatform(self, arr, dep):
        arr.sort()
        dep.sort()
        
        n = len(arr)
        platforms = 0
        max_platforms = 0
        i, j = 0, 0
        
        while i < n:
            if arr[i] <= dep[j]:  # A train is arriving
                platforms += 1
                max_platforms = max(max_platforms, platforms)
                i += 1
            else:  # A train is departing
                platforms -= 1
                j += 1
        
        return max_platforms
