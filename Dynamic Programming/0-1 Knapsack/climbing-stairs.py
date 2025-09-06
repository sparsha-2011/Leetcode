# Author: Sparsha Srinath
# Date: 2025-08-19
# Problem: Climbing Stairs
# Link: https://leetcode.com/problems/climbing-stairs/
# Tags: Dynamic Programming, Fibonacci
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases: if n <= 2, the number of ways equals n
        # (1 step: 1 way, 2 steps: 2 ways -> (1+1), (2))
        if n <= 2:
            return n

        # dp[i] = number of distinct ways to reach step i
        dp = [0] * (n + 1)

        # Initialization:
        # 1 way to stay at the ground (step 0)
        # 1 way to climb 1 step
        dp[0], dp[1] = 1, 1

        # Fill dp array using the relation:
        # dp[i] = dp[i-1] + dp[i-2]
        # Explanation: To reach step i, you can come from step i-1 (1 step)
        # or from step i-2 (2 steps).
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        # Return the number of ways to reach step n
        return dp[n]
