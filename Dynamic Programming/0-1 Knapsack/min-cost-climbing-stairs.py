# Author: Sparsha Srinath
# Date: 2025-08-19
# Problem: Min Cost Climbing Stairs
# Link: https://leetcode.com/problems/min-cost-climbing-stairs/
# Tags: Dynamic Programming, Array
# Time Complexity: O(N)
# Space Complexity: O(N)

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        # If only 2 steps, the cheaper one is the answer
        if n == 2:
            return min(cost[0], cost[1])

        # dp[i] = minimum cost to reach step i
        dp = [0] * n

        # Base cases: directly take first or second step
        dp[0], dp[1] = cost[0], cost[1]

        # Fill dp array
        # At each step, you can come from one step below or two steps below
        for i in range(2, n):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

        # Final answer: reaching the "top" which is beyond the last step
        return min(dp[n - 1], dp[n - 2])
