# Author: Sparsha Srinath  
# Date: 2025-06-29  
# Problem: Container With Most Water  
# Source: Leetcode - https://leetcode.com/problems/container-with-most-water/  
# Tags: Two Pointers, Greedy, Array  
# Time Complexity: O(n)  
# Space Complexity: O(1)

from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l, r = 0, len(heights) - 1  # Initialize two pointers at both ends

        while l < r:
            # Calculate the area with the shorter of the two heights
            height = min(heights[l], heights[r])
            width = r - l
            max_area = max(max_area, height * width)

            # Move the pointer at the shorter line inward to try a potentially larger area
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return max_area
