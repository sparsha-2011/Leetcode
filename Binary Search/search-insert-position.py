
# Author: Sparsha Srinath
# Date: 2025-08-10
# Problem: Search Insert Position
# Link: https://leetcode.com/problems/search-insert-position/
# Tags: Binary Search, Array
# Time Complexity: O(log n) - Binary search over sorted array
# Space Complexity: O(1) - Constant extra space


from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        N = len(nums)
        start = 0
        end  = N - 1
        res = N
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                res = mid
                end = mid - 1
        return res
