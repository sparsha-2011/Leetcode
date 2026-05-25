```python
# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/task-scheduler-ii/
# Date: 2026-05-24
# Tags: arrays, hash-map, simulation, greedy
# Description:
#   Given tasks that must be completed in order and a minimum space (cooldown)
#   between same-type tasks, find the minimum days to complete all tasks.
#   Unlike Task Scheduler I, tasks must be done in order — no rearranging.
#   Use a hashmap to track the last day each task type was completed.
#   If the cooldown hasn't passed, skip days forward until it has.
#
# Input: tasks (List[int]), space (int)
# Output: int — minimum number of days
#
# Example:
#   Input : tasks=[1,2,1,2,3,1], space=3
#   Output: 9
#
# Time Complexity : O(n) — single pass through tasks
# Space Complexity: O(n) — hashmap storing last day per task type

from typing import List

class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        day = 0
        prev = {}
        for tsk in tasks:
            day += 1
            if tsk in prev:
                days_passed = day - prev[tsk]
                if days_passed <= space:
                    day += space - days_passed + 1
            prev[tsk] = day
        return day
```
