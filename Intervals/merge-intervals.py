# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/merge-intervals/
# Date: 2025-06-15
# Tags: arrays, sorting, greedy, intervals, list-manipulation

# Description:
#   Given a collection of intervals, this function merges all overlapping intervals.
#   It first sorts the intervals by their start times, then iteratively merges overlapping intervals 
#   using a greedy approach by comparing the current interval with the last one in the result list.
#
# Input: List of intervals represented as [start, end]
# Output: List of merged non-overlapping intervals
#
# Example:
#   Input : [[1,3],[2,6],[8,10],[15,18]]
#   Output: [[1,6],[8,10],[15,18]]
#
# Time Complexity : O(n log n) due to sorting
# Space Complexity: O(n) for storing the result

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])  # Sort by start time
        result = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = result[-1][1]
            if start <= lastEnd:
                result[-1][1] = max(lastEnd, end)  # Merge intervals
            else:
                result.append([start, end])  # Add new interval

        return result
