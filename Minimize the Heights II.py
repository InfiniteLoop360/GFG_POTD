class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        if n == 1:
            return 0
        
        # Step 1: Sort the array
        arr.sort()
        
        # Step 2: Initial difference
        ans = arr[-1] - arr[0]
        
        # Step 3: Initial small and big after modifications
        small = arr[0] + k
        big = arr[-1] - k
        
        # Step 4: Traverse and minimize
        for i in range(n - 1):
            mini = min(small, arr[i+1] - k)
            maxi = max(big, arr[i] + k)
            
            if mini < 0:   # skip invalid (no negative heights allowed)
                continue
            
            ans = min(ans, maxi - mini)
        
        return ans
