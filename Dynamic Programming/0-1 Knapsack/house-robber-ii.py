# Author: Sparsha Srinath
# Date: 2025-08-19
# Problem: House Robber II
# Link: https://leetcode.com/problems/house-robber-ii/
# Tags: Dynamic Programming, Array
# Time Complexity: O(N)
# Space Complexity: O(N)

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge case: only one house
        if len(nums) == 1:
            return nums[0]

        # Helper function: linear version of house robber
        def rob_linear(nums: List[int]) -> int:
            n = len(nums)

            # If only one house in this slice
            if n == 1:
                return nums[0]

            # dp[i] = max robbed amount from first i houses in this slice
            dp = [0] * n

            # Base initialization
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            # Fill DP array
            for i in range(2, n):
                # Either rob current house or skip it
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

            return dp[n - 1]

        # Since it's circular, we cannot rob both the first and last house
        # Case 1: Rob houses from index 1 to n-1
        rob1 = rob_linear(nums[1:])

        # Case 2: Rob houses from index 0 to n-2
        rob2 = rob_linear(nums[:len(nums) - 1])

        # Final answer: maximum of both cases
        return max(rob1, rob2)
