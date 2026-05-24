# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/maximum-performance-of-a-team/
# Date: 2025-06-15
# Tags: arrays, sorting, heap, greedy, priority-queue
# Description:
#   Given n engineers with individual speed and efficiency values, select at most k
#   engineers to maximize team performance, defined as sum(speeds) * min(efficiency).
#   Sort engineers by efficiency descending so the current engineer always sets the
#   minimum efficiency. Use a min-heap to maintain the top-k speeds seen so far,
#   dropping the smallest speed when the heap exceeds k. At each step, compute
#   performance and track the global maximum.
#
# Input: n (int), speed (List[int]), efficiency (List[int]), k (int)
# Output: int — maximum performance modulo 10^9 + 7
#
# Example:
#   Input : n=6, speed=[2,10,3,1,5,8], efficiency=[5,4,3,9,7,2], k=2
#   Output: 60
#
# Time Complexity : O(n log n) for sorting + O(n log k) for heap operations
# Space Complexity: O(n) for sorted pairs + O(k) for the heap

import heapq
from typing import List

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        minHeap = []
        speed_sum = 0
        performance = 0
        max_performance = 0

        engineers = sorted(zip(efficiency, speed), reverse=True)
        for ef, sp in engineers:
            speed_sum += sp
            heapq.heappush(minHeap, sp)
            if len(minHeap) > k:
                min_sp = heapq.heappop(minHeap)
                speed_sum -= min_sp
            
            performance = speed_sum * ef
            max_performance = max(max_performance, performance)
        
        return max_performance % (10**9 + 7)
