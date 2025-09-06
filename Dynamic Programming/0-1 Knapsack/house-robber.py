# Author: Sparsha Srinath
# Date: 2025-08-19
# Problem: House Robber
# Link: https://leetcode.com/problems/house-robber/
# Tags: Dynamic Programming, Array
# Time Complexity: O(N)
# Space Complexity: O(N)

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # Base case: only one house
        if n == 1:
            return nums[0]

        # dp[i] = max amount robbed from first i houses (0-indexed)
        dp = [0] * n

        # Base initialization
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # Fill DP table
        for i in range(2, n):
            # Either rob current house and add dp[i-2], or skip current (take dp[i-1])
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        # Final answer is max robbed amount till the last house
        return dp[n - 1]
