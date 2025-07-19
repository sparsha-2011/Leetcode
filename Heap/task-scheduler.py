# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/task-scheduler/
# Date: 2025-06-15
# Tags: heap, greedy, priority-queue, task-scheduling, simulation
#
# Description:
#   Given a list of tasks and an integer n representing the cooldown period,
#   schedule the tasks so that the same task is at least n units apart.
#   Return the least amount of time required to finish all tasks.
#
#   Approach:
#     - Build a frequency map (dict) of tasks.
#     - Use a max-heap to always schedule the most frequent available task.
#     - Use a queue to track cooldowns: [remaining_count, available_time].
#     - Simulate time or fast-forward when idle.
#
# Time Complexity: O(n * log k)
# Space Complexity: O(k)

import heapq
from typing import List
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Build a frequency dictionary
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1

        # Step 2: Create a max-heap of negative frequencies
        maxHeap = [-count for count in freq.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # format: [remaining_count, next_available_time]

        while maxHeap or q:
            time += 1

            # If we can run a task, do it
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)  # Add because cnt is negative
                if cnt:
                    # Put it in cooldown
                    q.append([cnt, time + n])

            # If the front task in queue is ready to be scheduled again
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time


