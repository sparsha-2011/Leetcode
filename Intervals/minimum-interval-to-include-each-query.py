# Author: Sparsha Srinath  
# URL: https://leetcode.com/problems/minimum-interval-to-include-each-query/  
# Date: 2025-06-15  
# Tags: greedy, heap, sorting, intervals, binary-search, priority-queue, arrays  

# Description:
#   For each query, find the length of the smallest interval from a list of intervals
#   such that the interval contains the query point. If no such interval exists, return -1.
#
# Approach:
#   - Sort intervals by start time
#   - Sort queries to process in increasing order
#   - Use a min-heap to track all intervals that include the current query
#     (heap stores: (interval_length, interval_end))
#   - As we move through queries:
#       - Add all intervals starting before or at the query
#       - Remove all intervals that end before the query
#       - The top of the heap gives the smallest-length interval covering the query
#   - Store results in a map, then return them in original query order
#
# Input:
#   intervals: List[List[int]] - list of [start, end] intervals
#   queries: List[int] - list of integer query points
#
# Output:
#   List[int] - list of smallest interval lengths (or -1 if no interval contains the query)
#
# Example:
#   Input : intervals = [[1,4],[2,4],[3,6],[2,5]], queries = [2,3,4,5]
#   Output: [3,3,3,4]
#
# Time Complexity: O((n + m) log n), where n = len(intervals), m = len(queries)
# Space Complexity: O(n + m)

from typing import List
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()  # Sort intervals by start
        res = {}
        minHeap = []  # (interval_length, interval_end)
        i = 0

        for q in sorted(queries):
            # Add all intervals where start <= query
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1
            
            # Remove intervals that end before the query
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            res[q] = minHeap[0][0] if minHeap else -1

        return [res[q] for q in queries]
