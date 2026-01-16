class Solution:
    def minMen(self, arr):
        n = len(arr)
        intervals = []
        
        # Step 1: Build intervals
        for i in range(n):
            if arr[i] != -1:
                start = max(0, i - arr[i])
                end = min(n - 1, i + arr[i])
                intervals.append((start, end))
        
        # Step 2: Sort intervals
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        count = 0
        idx = 0
        covered = 0
        
        # Step 3: Greedy covering
        while covered < n:
            farthest = covered
            
            while idx < len(intervals) and intervals[idx][0] <= covered:
                farthest = max(farthest, intervals[idx][1] + 1)
                idx += 1
            
            if farthest == covered:
                return -1
            
            count += 1
            covered = farthest
        
        return count
