class Solution:
    def assignHole(self, mices, holes):
        # Step 1: Sort both arrays
        mices.sort()
        holes.sort()
        
        # Step 2: Compute max distance
        max_time = 0
        for i in range(len(mices)):
            max_time = max(max_time, abs(mices[i] - holes[i]))
        
        return max_time
