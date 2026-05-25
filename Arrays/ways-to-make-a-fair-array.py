# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/ways-to-make-a-fair-array/
# Date: 2026-05-24
# Tags: arrays, prefix-sum, math
# Description:
#   Given an array, count how many indices can be removed to make the array "fair"
#   (even-indexed sum equals odd-indexed sum). When an element is removed, everything
#   to the right shifts left — so right-side even indices become odd and vice versa.
#   Use prefix sums for even and odd indices separately. For each removal candidate,
#   left side stays the same, right side even↔odd swap. Check if new sums are equal.
#
# Input: nums (List[int])
# Output: int — number of fair removal indices
#
# Example:
#   Input : nums=[2,1,6,4]
#   Output: 1 (removing index 1 gives [2,6,4] where even=2+4=6, odd=6)
#
# Time Complexity : O(n) — two passes (compute totals + check each index)
# Space Complexity: O(1) — only tracking running sums

from typing import List

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        total_even = 0
        for i in range(0, len(nums), 2):
            total_even += nums[i]
        total_odd = total_sum - total_even
        count = 0
        left_even = 0
        left_odd = 0
        for i in range(len(nums)):

            if i % 2 == 0:
                right_even = total_even - left_even - nums[i]
                right_odd = total_odd - left_odd
            else:
                right_even = total_even - left_even
                right_odd = total_odd - left_odd - nums[i]

            new_even = left_even + right_odd
            new_odd = left_odd + right_even
            if new_even == new_odd:
                count += 1

            if i % 2 == 0:
                left_even += nums[i]
            else:
                left_odd += nums[i]

        return count
