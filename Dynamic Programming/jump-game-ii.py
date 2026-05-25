# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/jump-game-ii/
# Date: 2026-05-24
# Tags: arrays, greedy, bfs
# Description:
#   Given an array where each element is the max jump length from that position,
#   find the minimum number of jumps to reach the last index. Uses a greedy BFS
#   approach: treat each jump as a level. Track the farthest reachable position
#   within the current level. When you hit the end of the current level (i == end),
#   take the next jump and update end to farthest.
#
#   Visualization with nums = [2, 3, 1, 1, 4]:
#     [0] [1, 2] [3, 4]
#      ^   ^^^^^  ^^^^^
#    start jump1  jump2 → answer: 2
#
# Input: nums (List[int])
# Output: int — minimum number of jumps to reach last index
#
# Example:
#   Input : nums=[2,3,1,1,4]
#   Output: 2
#
# Time Complexity : O(n) — single pass
# Space Complexity: O(1) — only tracking three variables

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        n = len(nums) - 1
        cnt = 0
        end = 0
        for i in range(n):
            farthest = max(farthest, i + nums[i])

            if i == end:
                cnt += 1
                end = farthest

        return cnt
