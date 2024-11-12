class Solution:
    def canAttend(self, arr):
        # Step 1: Sort the meetings by their start times
        arr.sort(key=lambda x: x[0])

        # Step 2: Check for any overlapping meetings
        for i in range(1, len(arr)):
            if arr[i][0] < arr[i - 1][1]:  # Current start < previous end
                return False

        return True
