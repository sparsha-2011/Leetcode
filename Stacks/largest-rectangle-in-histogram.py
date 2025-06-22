# Author: Sparsha Srinath  
# URL: https://leetcode.com/problems/largest-rectangle-in-histogram/  
# Date: 2025-06-15  
# Tags: monotonic-stack, arrays, greedy, histogram, stack  

# Description:
#   Given a list of bar heights in a histogram, return the area of the largest rectangle that can be formed.
#   Each bar has a width of 1 unit. The goal is to find the maximal area formed using consecutive bars.
#
# Approach:
#   - For each bar, find the index of the nearest smaller bar to the left (NSL)
#     and the nearest smaller bar to the right (NSR)
#   - The width of the largest rectangle that includes the current bar is (NSR - NSL - 1)
#   - Use a monotonic increasing stack to compute NSL and NSR in O(n)
#
# Input: heights: List[int] — heights of histogram bars
# Output: int — area of the largest rectangle
#
# Example:
#   Input : [2,1,5,6,2,3]
#   Output: 10  # from bars 5 and 6 (area = 2 * 5)
#
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        NSL = [0] * N  # Nearest Smaller to Left
        NSR = [0] * N  # Nearest Smaller to Right
        stack = []

        # Compute NSL
        for i in range(N):
            while stack and stack[-1][1] >= heights[i]:
                stack.pop()
            if not stack:
                NSL[i] = -1
            else:
                NSL[i] = stack[-1][0]
            stack.append((i, heights[i]))

        # Reset and compute NSR
        stack = []
        for i in range(N - 1, -1, -1):
            while stack and stack[-1][1] >= heights[i]:
                stack.pop()
            if not stack:
                NSR[i] = N
            else:
                NSR[i] = stack[-1][0]
            stack.append((i, heights[i]))

        # Compute max area
        maxArea = 0
        for i in range(N):
            width = NSR[i] - NSL[i] - 1
            maxArea = max(maxArea, heights[i] * width)

        return maxArea
