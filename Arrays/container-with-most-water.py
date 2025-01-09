# Problem Title: Container With Most Water
# Problem URL: https://leetcode.com/problems/container-with-most-water/
# Difficulty: Medium

"""
Problem Statement:

You are given an integer array heights where heights[i] represents the height of the i-th bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:

Input: height = [1,7,2,5,4,7,3,6]

Output: 36

Example 2:

Input: height = [2,2,2]

Output: 4

Constraints:

2 <= height.length <= 1000
0 <= height[i] <= 1000
"""

from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Initialize two pointers: one at the left end, one at the right end
        l, r = 0, len(heights) - 1
        max_area = 0
        
        # Use the two-pointer approach to calculate the area
        while l < r:
            # Calculate the area formed by the bars at the two pointers
            area = min(heights[l], heights[r]) * (r - l)
            max_area = max(max_area, area)

            # Move the pointer pointing to the shorter bar towards the other pointer
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_area
