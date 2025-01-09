# Problem Title: Trapping Rain Water
# Problem URL: https://leetcode.com/problems/trapping-rain-water/
# Difficulty: Hard

"""
Problem Statement:

You are given an array of non-negative integers height which represent an elevation map.
Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.

Example 1:

Input: height = [0,2,0,3,1,0,1,3,2,1]

Output: 9

Constraints:

1 <= height.length <= 1000
0 <= height[i] <= 1000
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # Edge case: If height is empty, return 0
        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        res = 0
        
        # Two-pointer approach to calculate trapped water
        while l < r:
            if leftMax < rightMax:
                # Move left pointer to the right
                l += 1
                # Update the leftMax to the maximum of the current leftMax and height[l]
                leftMax = max(leftMax, height[l])
                # Calculate trapped water at the current position
                res += leftMax - height[l]
            else:
                # Move right pointer to the left
                r -= 1
                # Update the rightMax to the maximum of the current rightMax and height[r]
                rightMax = max(rightMax, height[r])
                # Calculate trapped water at the current position
                res += rightMax - height[r]
        
        return res
