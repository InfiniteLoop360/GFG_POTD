class Solution:
    def mergeOverlap(self, arr):
        # Sort intervals based on the start time
        arr.sort(key=lambda x: x[0])
        merged = []

        for interval in arr:
            # If the merged list is empty or there is no overlap, add the interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Merge the intervals
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
