# Author: Sparsha Srinath
# Date: 2025-08-19
# Problem: Target Sum (Number of Ways to Assign Symbols to Make Target Sum)
# Link: https://leetcode.com/problems/target-sum/
# Tags: Dynamic Programming, Subset Sum, Partition DP
# Time Complexity: O(N * M)  where M = (target + sum(nums)) // 2
# Space Complexity: O(N * M)

from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # If absolute target is greater than total sum,
        # or (target + sum(nums)) is odd, no valid partition exists.
        if abs(target) > sum(nums) or (target + sum(nums)) % 2 != 0:
            return 0 
        
        # Transform problem into subset sum:
        # Find number of subsets with sum = (target + sum(nums)) // 2
        m = (target + sum(nums)) // 2

        # dp[i][j] = number of ways to achieve sum j using first i numbers
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Base case: one way to make sum = 0 (take empty subset)
        dp[0][0] = 1

        # Fill DP table
        for i in range(1, n + 1):
            for j in range(m + 1):
                if nums[i - 1] <= j:
                    # Either include nums[i-1] or exclude it
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
                else:
                    # Can't include nums[i-1], so only exclude
                    dp[i][j] = dp[i - 1][j]
        
        # Answer: number of subsets achieving target sum
        return dp[n][m]
