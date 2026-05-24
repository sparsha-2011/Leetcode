# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/sliding-window-median/
# Date: 2025-06-15
# Tags: arrays, sliding-window, heap, priority-queue, two-heaps, lazy-deletion
# Description:
#   Given an array of integers and a window size k, return the median of each
#   sliding window. Uses two heaps (max-heap for lower half, min-heap for upper
#   half) with lazy deletion. When an element leaves the window, it is marked in
#   a delayed hashmap rather than immediately removed from the heap. Stale elements
#   are cleaned up when they surface to the top. Manual size tracking ensures
#   accurate rebalancing despite stale elements in the heaps.
#
# Input: nums (List[int]), k (int)
# Output: List[float] — median of each window
#
# Example:
#   Input : nums=[1,3,-1,-3,5,3,6,7], k=3
#   Output: [1.0,-1.0,-1.0,3.0,5.0,6.0]
#
# Time Complexity : O(n log n) for heap operations across all windows
# Space Complexity: O(n) for heaps and delayed map

import heapq
from collections import defaultdict
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        max_heap = []  # lower half (negated)
        min_heap = []  # upper half
        delayed = defaultdict(int)
        lower_size = 0
        upper_size = 0
        result = []

        def add(value):
            nonlocal lower_size, upper_size
            if not max_heap or value <= -max_heap[0]:
                heapq.heappush(max_heap, -value)
                lower_size += 1
            else:
                heapq.heappush(min_heap, value)
                upper_size += 1

        def remove(value):
            nonlocal lower_size, upper_size
            delayed[value] += 1
            if value <= -max_heap[0]:
                lower_size -= 1
            else:
                upper_size -= 1

        def rebalance():
            nonlocal lower_size, upper_size
            while lower_size > upper_size + 1:
                val = -heapq.heappop(max_heap)
                heapq.heappush(min_heap, val)
                lower_size -= 1
                upper_size += 1
                cleanup()
            while upper_size > lower_size:
                val = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -val)
                upper_size -= 1
                lower_size += 1
                cleanup()

        def cleanup():
            while max_heap and delayed[-max_heap[0]] > 0:
                delayed[-max_heap[0]] -= 1
                heapq.heappop(max_heap)
            while min_heap and delayed[min_heap[0]] > 0:
                delayed[min_heap[0]] -= 1
                heapq.heappop(min_heap)

        def get_median():
            if k % 2 == 1:
                return float(-max_heap[0])
            else:
                return (-max_heap[0] + min_heap[0]) / 2.0

        # Add first k elements
        for i in range(k):
            add(nums[i])
        rebalance()
        cleanup()
        result.append(get_median())

        # Slide the window
        for i in range(k, len(nums)):
            add(nums[i])
            remove(nums[i - k])
            rebalance()
            cleanup()
            result.append(get_median())

        return result
