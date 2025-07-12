# Author: Sparsha Srinath  
# Date: 2025-07-11  
# LeetCode URL: https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/  
# Tags: sliding-window, hashset, prefix-sum, arrays, optimization  
#
# Description:
#   Given an integer array `nums` and an integer `k`, return the maximum sum of a subarray
#   of length `k` with all distinct elements. If no such subarray exists, return 0.
#
# Approach:
#   - Use the sliding window technique with a hash set to ensure all elements are distinct
#   - Maintain a running sum (`cur_sum`) and update it as the window shifts
#   - If a duplicate is encountered, shrink the window from the left
#   - If window size reaches `k`, check and update `max_sum`
#   - Then shrink the window to continue sliding

from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        start = 0
        max_sum = 0
        cur_sum = 0
        elements = set()

        for end in range(len(nums)):
            # Shrink window if duplicate found
            while nums[end] in elements:
                cur_sum -= nums[start]
                elements.remove(nums[start])
                start += 1

            # Add current number
            cur_sum += nums[end]
            elements.add(nums[end])

            # If window size is k, check for max and slide window
            if end - start + 1 == k:
                max_sum = max(max_sum, cur_sum)
                cur_sum -= nums[start]
                elements.remove(nums[start])
                start += 1

        return max_sum
