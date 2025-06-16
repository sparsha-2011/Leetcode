
# Author      : Sparsha Srinath
# Date        : June 15, 2025
# Title       : Meeting Room Assignment
# Description : 
#   Given a list of meeting intervals with start and end times, this script 
#   determines the minimum number of meeting rooms required and assigns each 
#   meeting to a specific room such that no two meetings in the same room overlap.
#
#   This approach uses a min-heap to track ongoing meetings and efficiently 
#   reuses rooms that become free, ensuring optimal room allocation.
#
# Input  : List of Interval(start, end)
# Output : 
#   - Total number of rooms required
#   - List of room assignments (by original input order)
#
# Example:
#   Input  : [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
#   Output : 2 rooms needed, Room assignments = [0, 1, 1]
#
# Tags: heapq, intervals



import heapq

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRoomsWithAssignment(self, intervals: List[Interval]) -> Tuple[int, List[int]]:
        intervals = sorted(enumerate(intervals), key=lambda x: x[1].start)
        # Format: (end_time, room_number)
        min_heap = []
        
        room_counter = 0  # Next new room number
        room_map = {}     # interval index -> room number
        available_rooms = []  # Track released rooms for reuse

        for idx, interval in intervals:
            # Free up rooms that have finished before current meeting starts
            while min_heap and min_heap[0][0] <= interval.start:
                _, freed_room = heapq.heappop(min_heap)
                heapq.heappush(available_rooms, freed_room)

            # Assign room
            if available_rooms:
                assigned_room = heapq.heappop(available_rooms)
            else:
                assigned_room = room_counter
                room_counter += 1

            heapq.heappush(min_heap, (interval.end, assigned_room))
            room_map[idx] = assigned_room

        # Convert mapping to room list by input order
        room_assignment = [room_map[i] for i in range(len(intervals))]
        return room_counter, room_assignment
