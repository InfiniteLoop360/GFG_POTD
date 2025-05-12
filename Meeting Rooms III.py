import heapq

class Solution:
    def mostBooked(self, n, meetings):
        # Sort meetings by start time
        meetings.sort()
        
        # Heap of available rooms (min-heap by room number)
        available_rooms = list(range(n))
        heapq.heapify(available_rooms)
        
        # Min-heap of ongoing meetings (end_time, room_number)
        ongoing_meetings = []
        
        # Count of meetings for each room
        room_counts = [0] * n
        
        for start, end in meetings:
            # Free up rooms that have completed meetings by current start time
            while ongoing_meetings and ongoing_meetings[0][0] <= start:
                end_time, room_number = heapq.heappop(ongoing_meetings)
                heapq.heappush(available_rooms, room_number)
            
            duration = end - start
            
            if available_rooms:
                # Assign to the available room with the smallest number
                room = heapq.heappop(available_rooms)
                heapq.heappush(ongoing_meetings, (end, room))
                room_counts[room] += 1
            else:
                # No room is free: delay the meeting
                end_time, room = heapq.heappop(ongoing_meetings)
                heapq.heappush(ongoing_meetings, (end_time + duration, room))
                room_counts[room] += 1

        # Find the room with the maximum meetings
        max_meetings = max(room_counts)
        for i, count in enumerate(room_counts):
            if count == max_meetings:
                return i
