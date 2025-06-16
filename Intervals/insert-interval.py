# Author: Sparsha Srinath  
# URL: https://leetcode.com/problems/insert-interval/  
# Date: 2025-06-15  
# Tags: intervals, arrays, sorting, merge-intervals, greedy, list-manipulation  

# Description:
#   Given a list of non-overlapping intervals sorted by their start times, and a new interval, 
#   insert the new interval into the list (merge if necessary) and return the updated list of intervals.
#   
#   The approach:
#     - Sort the input intervals by start time
#     - Iterate through the intervals:
#         - If newInterval ends before the current starts: insert and return result + remaining
#         - If newInterval starts after the current ends: add the current interval to result
#         - Else: merge overlapping intervals by updating newInterval bounds
#     - After the loop, append any remaining newInterval
#
# Input: 
#   intervals: List[List[int]] — list of non-overlapping intervals
#   newInterval: List[int] — interval to insert
# Output: 
#   List[List[int]] — updated interval list after insertion and merging
#
# Example:
#   Input : intervals = [[1,3],[6,9]], newInterval = [2,5]
#   Output: [[1,5],[6,9]]
#
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        
        for i in range(len(intervals)):
            start, end = intervals[i]
            
            if newInterval[1] < start:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > end:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], start), max(newInterval[1], end)]
        
        res.append(newInterval)
        return res
