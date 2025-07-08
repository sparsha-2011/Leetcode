# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/last-stone-weight/
# Date: 2025-06-15
# Tags: heap, priority-queue, simulation, greedy, max-heap
#
# Description:
#   You are given a list of stones with positive integer weights. In each turn:
#     - Pick the two heaviest stones (x and y)
#     - Smash them together:
#         - If x == y: both are destroyed
#         - If x != y: the remaining weight (|x - y|) is added back
#   Repeat until at most one stone remains.
#
#   Return the weight of the last remaining stone (or 0 if none remain).
#
#   Approach:
#     - Use a max-heap to efficiently get the heaviest stones.
#     - Python's heapq is a min-heap, so invert values to simulate a max-heap.
#
# Input:
#   stones: List[int] — the list of stone weights
# Output:
#   int — the weight of the last remaining stone, or 0
#
# Example:
#   Input : stones = [2,7,4,1,8,1]
#   Output: 1
#
# Time Complexity: O(n log n)
# Space Complexity: O(n)

import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Invert stone weights to simulate max-heap
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        # Repeat until at most one stone remains
        while len(max_heap) >= 2:
            x = -heapq.heappop(max_heap)  # heaviest
            y = -heapq.heappop(max_heap)  # second heaviest
            if x != y:
                heapq.heappush(max_heap, -(x - y))

        return -max_heap[0] if max_heap else 0


# -----------------------------
# Optional test case to run
# -----------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.lastStoneWeight([2, 7, 4, 1, 8, 1]))  # Output: 1
