class Solution:
    def powerfulInteger(self, intervals, k):
        events = []

        for start, end in intervals:
            events.append((start, 1))       # +1 when interval starts
            events.append((end + 1, -1))    # -1 after interval ends

        events.sort()

        active = 0
        max_powerful = -1

        for i in range(len(events) - 1):
            active += events[i][1]
            if active >= k:
                max_powerful = max(max_powerful, events[i + 1][0] - 1)

        return max_powerful
