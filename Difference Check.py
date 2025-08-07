class Solution:
    def minDifference(self, arr):
        def to_seconds(time_str):
            h, m, s = map(int, time_str.split(":"))
            return h * 3600 + m * 60 + s

        # Step 1: Convert all times to seconds
        seconds = [to_seconds(t) for t in arr]

        # Step 2: Sort the times
        seconds.sort()

        # Step 3: Initialize min_diff to a large number
        min_diff = float('inf')

        # Step 4: Compare adjacent times
        for i in range(1, len(seconds)):
            diff = seconds[i] - seconds[i - 1]
            min_diff = min(min_diff, diff)

        # Step 5: Check the wrap-around case (from last to first across midnight)
        wrap_diff = 86400 - seconds[-1] + seconds[0]  # Total seconds in a day is 86400
        min_diff = min(min_diff, wrap_diff)

        return min_diff
