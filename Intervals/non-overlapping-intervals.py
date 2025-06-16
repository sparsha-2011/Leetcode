# Author: Sparsha Srinath  
# URL: https://leetcode.com/problems/non-overlapping-intervals/  
# Date: 2025-06-15  
# Tags: greedy, sorting, intervals, arrays, list-manipulation  

# Description:
#   Given a collection of intervals, find the minimum number of intervals you need to remove 
#   to make the rest of the intervals non-overlapping.
#   
#   The strategy is to:
#     - Sort intervals by their end times (greedy)
#     - Iterate through the sorted list and count how many intervals overlap
#     - Only update the `prevEnd` when there's no overlap (i.e., interval is kept)
#
# Input: List of intervals [start, end]
# Output: Integer - minimum number of intervals to remove
#
# Example:
#   Input : [[1,2],[2,3],[3,4],[1,3]]
#   Output: 1
#
# Time Complexity : O(n log n) due to sorting
# Space Complexity: O(1) if ignoring output list, O(n) if storing result list

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])  # Sort by end time
        prevEnd = intervals[0][1]
        cnt = 0

        for start, end in intervals[1:]:
            if start < prevEnd:
                cnt += 1  # Overlap found, remove this interval
            else:
                prevEnd = end  # No overlap, update end tracker

        return cnt
