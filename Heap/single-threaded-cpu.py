# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/single-threaded-cpu/
# Date: 2025-06-15
# Tags: arrays, sorting, heap, priority-queue, simulation
# Description:
#   Given a list of tasks where each task has an enqueue time and processing time,
#   simulate a single-threaded CPU that picks the available task with the shortest
#   processing time (ties broken by lowest index). Sort tasks by enqueue time, then
#   use a min-heap to track available tasks ordered by (processing_time, index).
#   When no tasks are available, jump time forward to the next arrival.
#
# Input: tasks (List[List[int]]) — each task is [enqueueTime, processingTime]
# Output: List[int] — order in which tasks are processed (by original index)
#
# Example:
#   Input : tasks=[[1,2],[2,4],[3,2],[4,1]]
#   Output: [0,2,3,1]
#
# Time Complexity : O(n log n) for sorting and heap operations
# Space Complexity: O(n) for sorted tasks and heap

import heapq
from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # pair tasks with original index, sort by enqueue time
        sorted_tasks = sorted([(et, pt, i) for i, (et, pt) in enumerate(tasks)])
        
        result = []
        available = []  # min-heap of (processing_time, index)
        time = 0
        i = 0
        
        while i < len(sorted_tasks) or available:
            # add all tasks that have arrived by current time
            while i < len(sorted_tasks) and sorted_tasks[i][0] <= time:
                et, pt, ind = sorted_tasks[i]
                heapq.heappush(available, (pt, ind))
                i += 1
            
            if available:
                pt, ind = heapq.heappop(available)
                time += pt  # jump time forward by processing duration
                result.append(ind)
            else:
                # no tasks available, jump to next arrival
                time = sorted_tasks[i][0]
        
        return result
