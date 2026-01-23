
# Author: Sparsha Srinath
# Date: 2025-08-10
# Problem: Find First and Last Position of Element in Sorted Array
# Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Tags: Binary Search, Array
# Time Complexity: O(log n) - Two binary searches
# Space Complexity: O(1) - Constant extra space


from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        first, last = -1, -1

        start = 0
        end = N - 1
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                first = mid
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1

        start = 0
        end = N - 1
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                last = mid
                start = mid + 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1

        return [first, last]
