# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/jump-game/
# Date: 2026-05-24
# Tags: arrays, greedy, dynamic-programming
# Description:
#   Given an array where each element is the max jump length from that position,
#   determine if you can reach the last index from index 0. Use a greedy approach
#   working backwards: track the leftmost position (goal) that can reach the end.
#   If a position can reach the current goal, it becomes the new goal. If goal
#   reaches 0, the start can reach the end.
#
#   DP intuition: dp[i] = can I reach the end from index i?
#   dp[i] = True if any of dp[i+1]...dp[i+nums[i]] is True → O(n²)
#   Greedy optimization: only track the leftmost True position → O(n)
#
# Input: nums (List[int])
# Output: bool — whether you can reach the last index
#
# Example:
#   Input : nums=[2,3,1,1,4]
#   Output: True (0→1→4 or 0→2→3→4)
#
#   Input : nums=[3,2,1,0,4]
#   Output: False (stuck at index 3)
#
# Time Complexity : O(n) — single pass backwards
# Space Complexity: O(1) — only tracking goal variable

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n - 1

        for i in range(n - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
