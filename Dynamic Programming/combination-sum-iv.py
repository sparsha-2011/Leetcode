# Date: 2025-04-15
# Author: Sparsha Srinath
# Leetcode (Combination Sum IV): https://leetcode.com/problems/combination-sum-iv/
# Tags: Dynamic Programming, 1D DP, Permutations, Memoization

from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        Given an array of distinct integers `nums` and a target integer `target`,
        return the number of possible combinations that add up to `target`.
        The order of numbers in the combinations matters.

        Args:
            nums (List[int]): List of distinct positive integers.
            target (int): Target sum to be formed.

        Returns:
            int: Number of permutations that sum to `target`.
        """

        # dp[i] will store the number of ways to reach sum i
        dp = [0] * (target + 1)

        # There's one way to make a total of 0 — by choosing nothing
        dp[0] = 1

        # Loop through each sub-target from 1 to target
        for total in range(1, target + 1):
            # Try every number in nums to form the current total
            for num in nums:
                if total - num >= 0:
                    # Add the number of ways to form (total - num)
                    dp[total] += dp[total - num]

        # The answer is the number of ways to form the full target
        return dp[target]
