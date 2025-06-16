# Author: Sparsha Srinath  
# URL: https://leetcode.com/problems/meeting-rooms-ii/  
# Date: 2025-06-15  
# Tags: intervals, greedy, two-pointers, arrays, sorting, sweep-line  

# Description:
#   Given an array of meeting time intervals consisting of start and end times, 
#   return the minimum number of conference rooms required.
#
# Approach (Sweep Line / Two-Pointer):
#   - Separate and sort start and end times independently
#   - Iterate through the start times:
#       - If a meeting starts before the earliest end, we need a new room
#       - Else, one meeting ended, so we free up a room
#   - Keep track of the max number of rooms used at any time
#
# Input:
#   intervals: List[Interval] — list of meeting intervals
# Output:
#   int — minimum number of rooms required
#
# Example:
#   Input : [[0,30],[5,10],[15,20]]
#   Output: 2
#
#   Input : [[7,10],[2,4]]
#   Output: 1
#
# Time Complexity: O(n log n) — sorting start and end arrays
# Space Complexity: O(n) — storing start and end times separately

from typing import List

# Definition of Interval
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        s = e = count = 0
        res = 0

        while s < len(intervals):
            if start[s] < end[e]:
                count += 1  # New room needed
                s += 1
            else:
                count -= 1  # Meeting ended, free a room
                e += 1
            res = max(res, count)

        return res

