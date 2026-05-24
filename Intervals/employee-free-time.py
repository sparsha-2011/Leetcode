# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/employee-free-time/
# Date: 2025-06-15
# Tags: arrays, sorting, greedy, intervals, merge-intervals
# Description:
#   Given a list of schedules for multiple employees, where each schedule is a list of
#   non-overlapping intervals representing working hours, this function finds the common
#   free time across all employees. It flattens all intervals, sorts by start time,
#   merges overlapping intervals, and then identifies the gaps between merged intervals.
#
# Input: List of lists of Interval objects representing each employee's working schedule
# Output: List of Interval objects representing common free time
#
# Example:
#   Input : [[[1,2],[5,6]], [[1,3]], [[4,10]]]
#   Output: [[3,4]]
#
# Time Complexity : O(n log n) due to sorting, where n is total number of intervals
# Space Complexity: O(n) for storing flattened and merged intervals


# Definition for an Interval.
class Interval:
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end

class Solution:
    def employeeFreeTime(self, schedule: list[list[Interval]]) -> list[Interval]:
        # your code here
        intervals = []

        for emp in schedule:
            for interval in emp:
                intervals.append(interval)
        
        intervals.sort(key=lambda l:l.start)

        non_overlap = [intervals[0]]

        for i in intervals[1:]:

            prevEnd = non_overlap[-1].end

            if i.start > prevEnd:
                non_overlap.append(i)  
            else:
                non_overlap[-1].end= max(prevEnd,i.end)
        
        result = []

        for i in range(1,len(non_overlap)):
            new = Interval(non_overlap[i-1].end,non_overlap[i].start)
            result.append(new)
        
        return result
