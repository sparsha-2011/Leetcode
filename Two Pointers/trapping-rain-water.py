# Author: Sparsha Srinath  
# Date: 2025-06-29  
# Problem: Trapping Rain Water  
# Source: Leetcode - https://leetcode.com/problems/trapping-rain-water/  
# Tags: Two Pointers, Dynamic Programming, Stack  
# Time Complexity: O(n)  
# Space Complexity: O(1)

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1  # Initialize two pointers
        leftMax, rightMax = height[l], height[r]  # Track the max heights from both ends
        res = 0  # Accumulate trapped water

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])  # Update left max
                res += leftMax - height[l]  # Water trapped at current l
            else:
                r -= 1
                rightMax = max(rightMax, height[r])  # Update right max
                res += rightMax - height[r]  # Water trapped at current r

        return res
