class Solution:
    def minRemoval(self, intervals):
        # Sorting intervals based on their ending times
        intervals.sort(key=lambda x: x[1])
        count, prev_end = 0, float('-inf')
        
        # Iterating through the intervals
        for start, end in intervals:
            if start >= prev_end:
                # Update previous end if there's no overlap
                prev_end = end
            else:
                # Count overlaps to be removed
                count += 1
        
        return count
