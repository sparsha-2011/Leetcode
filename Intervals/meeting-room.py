# Author: Sparsha Srinath  
# URL: https://leetcode.com/problems/meeting-rooms/  
# Date: 2025-06-15  
# Tags: intervals, greedy, sorting, arrays  

# Description:
#   Given an array of meeting time intervals consisting of start and end times, 
#   determine if a person could attend all meetings (i.e., no meetings overlap).
#
# Approach:
#   - Sort intervals by their end time (or start time, both work for this problem)
#   - Iterate through the sorted list and compare current start time with previous end time
#   - If there's any overlap, return False; otherwise, continue
#
# Input:
#   intervals: List[Interval] — list of meeting intervals
# Output:
#   bool — True if no overlaps (can attend all), False otherwise
#
# Example:
#   Input : [[0, 30], [5, 10], [15, 20]]
#   Output: False
#
#   Input : [[7, 10], [2, 4]]
#   Output: True
#
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1) if in-place sorting

from typing import List

# Definition of Interval
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        
        intervals.sort(key=lambda i: i.end)
        prevEnd = intervals[0].end

        for i in intervals[1:]:
            if i.start < prevEnd:
                return False
            prevEnd = i.end
            
        return True
