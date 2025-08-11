
# Author: Sparsha Srinath
# Date: 2025-08-10
# Problem: Find Minimum in Rotated Sorted Array
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Tags: Binary Search, Array
# Time Complexity: O(log n) - Modified binary search
# Space Complexity: O(1) - Constant space


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        end = n - 1

        while start <= end:
            # If the array segment is already sorted, start is the smallest
            if nums[start] <= nums[end]:
                return nums[start]

            mid = (start + end) // 2
            prev = (mid + n - 1) % n
            nxt = (mid + 1) % n

            # Check if mid is the rotation point (smallest element)
            if nums[mid] < nums[prev] and nums[mid] < nums[nxt]:
                return nums[mid]

            # Decide which half to search
            if nums[mid] >= nums[start]:  
                # Left half sorted, so pivot must be in right half
                start = mid + 1
            else:
                # Right half sorted, so pivot must be in left half
                end = mid - 1

        return nums[0]  # If no rotation
