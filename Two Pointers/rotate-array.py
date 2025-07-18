# Author: Sparsha Srinath  
# Date: 2025-06-29  
# Problem: Rotate Array  
# Source: Leetcode - https://leetcode.com/problems/rotate-array/  
# Tags: Array, Two Pointers, In-place  
# Time Complexity: O(n)  
# Space Complexity: O(1) — in-place rotation

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotates the array to the right by k steps, in-place.
        """
        k %= len(nums)  # Ensure k is within array bounds

        def reverse(left: int, right: int) -> None:
            """Helper function to reverse elements in-place."""
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # Step 1: Reverse the whole array
        reverse(0, len(nums) - 1)
        # Step 2: Reverse the first k elements
        reverse(0, k - 1)
        # Step 3: Reverse the remaining elements
        reverse(k, len(nums) - 1)
