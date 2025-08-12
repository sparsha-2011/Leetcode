# Author: Sparsha Srinath
# Date: 2025-08-11
# Problem: Find Peak Element
# Link: https://leetcode.com/problems/find-peak-element/
# Tags: Binary Search, Array
# Time Complexity: O(log n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)
        start, end = 0, N - 1

        while start < end:
            mid = (start + end) // 2

            if nums[mid] < nums[mid + 1]:
                # Peak is on the right side
                start = mid + 1
            else:
                # Peak is on the left side (including mid)
                end = mid

        return start
