class Solution:
    def insertInterval(self, intervals, newInterval):
        result = []
        i = 0
        n = len(intervals)

        # Add all intervals before the newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Merge overlapping intervals with the newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)

        # Add all intervals after the newInterval
        while i < n:
            result.append(intervals[i])
            i += 1

        return result