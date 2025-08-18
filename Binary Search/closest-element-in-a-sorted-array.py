# Author: Sparsha Srinath
# Date: 2025-08-17
# Problem: Closest Element in a Sorted Array
# Link: —
# Tags: Binary Search, Array
# Time Complexity: O(log n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def closestElement(self, nums: List[int], target: int) -> int:
        N = len(nums)
        start, end = 0, N - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return nums[mid]
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        # At this point, target is not in nums.
        # Possible candidates are nums[end] and nums[start] (if they exist).
        cand1 = nums[end] if end >= 0 else float('inf')
        cand2 = nums[start] if start < N else float('inf
