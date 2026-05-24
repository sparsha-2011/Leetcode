# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/mice-and-cheese/
# Date: 2025-06-15
# Tags: arrays, greedy, heap, priority-queue, sorting
# Description:
#   Two mice compete for n types of cheese. Mouse 1 earns reward1[i] and mouse 2
#   earns reward2[i] for eating cheese i. Mouse 1 must eat exactly k cheeses,
#   mouse 2 eats the rest. Start with sum(reward2) as a baseline (mouse 2 eats all),
#   then compute the gain of swapping each cheese to mouse 1: reward1[i] - reward2[i].
#   Use a min-heap to track the top-k gains and add them to the baseline.
#
# Input: reward1 (List[int]), reward2 (List[int]), k (int)
# Output: int — maximum total reward
#
# Example:
#   Input : reward1=[1,1,3,4], reward2=[4,4,1,1], k=2
#   Output: 15
#
# Time Complexity : O(n log k) for heap operations
# Space Complexity: O(k) for the heap

import heapq
from typing import List

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        minH = []
        max_reward = sum(reward2)

        for r1, r2 in zip(reward1, reward2):
            heapq.heappush(minH, (r1 - r2))
            while len(minH) > k:
                heapq.heappop(minH)

        return max_reward + sum(minH)
