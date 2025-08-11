
# Author: Sparsha Srinath
# Date: 2025-08-10
# Problem: Single Element in a Sorted Array
# Link: https://leetcode.com/problems/single-element-in-a-sorted-array/
# Tags: Binary Search, Array
# Time Complexity: O(log n) - Binary search halves the array each step
# Space Complexity: O(1) - Constant extra space


from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid

        return nums[left]
