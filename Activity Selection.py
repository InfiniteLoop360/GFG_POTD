class Solution:
    def activitySelection(self, start, finish):
        # Step 1: Sort activities based on finish time
        activities = sorted(zip(start, finish), key=lambda x: x[1])

        count = 1  # We can always select the first activity
        prev_end_time = activities[0][1]  # Store the end time of the first activity
        
        # Step 2: Iterate over sorted activities
        for i in range(1, len(activities)):
            s, f = activities[i]
            if s > prev_end_time:  # If current activity starts after previous one finishes
                count += 1
                prev_end_time = f  # Update the latest finish time
        
        return count  # Return max activities possible
