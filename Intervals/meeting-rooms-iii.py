# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/meeting-rooms-iii/
# Date: 2025-06-15
# Tags: arrays, sorting, heap, priority-queue, simulation
# Description:
#   Given n rooms (numbered 0 to n-1) and a list of meetings with start and end times,
#   assign each meeting to the lowest-numbered available room. If no room is available,
#   the meeting is delayed until the earliest room frees up (ties broken by lowest room
#   number). The meeting retains its original duration even when delayed. Return the
#   room number that held the most meetings.
#
# Input: n (int), meetings (List[List[int]])
# Output: int — room number with the most meetings
#
# Example:
#   Input : n=2, meetings=[[0,10],[1,5],[2,7],[3,4]]
#   Output: 0
#
# Time Complexity : O(m log n + m log m) where m = number of meetings, n = rooms
# Space Complexity: O(n) for the heaps

import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available = list(range(n))          # min-heap by room number
        busy = []                           # min-heap of (end_time, room_number)
        count = [0] * n

        for start, end in meetings:
            # free up rooms that have ended by this meeting's start
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                # no room free — wait for the earliest one
                earliest_end, room = heapq.heappop(busy)
                heapq.heappush(busy, (earliest_end + (end - start), room))

            count[room] += 1

        return count.index(max(count))
