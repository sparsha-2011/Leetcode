# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/maximum-gap/
# Date: 2026-05-24
# Tags: arrays, sorting, greedy
# Description:
#   Given an unsorted array, find the maximum difference between successive
#   elements in the sorted form. Sort the array, then iterate through
#   consecutive pairs tracking the largest gap.
#
# Input: nums (List[int])
# Output: int — maximum gap between successive elements in sorted order
#
# Example:
#   Input : nums=[3,6,9,1]
#   Output: 3 (sorted: [1,3,6,9] → gaps: 2,3,3 → max is 3)
#
# Time Complexity : O(n log n) — sorting
# Space Complexity: O(1) — only tracking gap variables

from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        max_gap = 0
        gap = 0
        nums.sort()
        pre = nums[0]

        for num in nums[1:]:
            gap = num - pre
            max_gap = max(max_gap, gap)
            pre = num
        return max_gap
