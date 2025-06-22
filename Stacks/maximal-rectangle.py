# Author: Sparsha Srinath  
# URL: https://leetcode.com/problems/maximal-rectangle/  
# Date: 2025-06-15  
# Tags: matrix, histogram, monotonic-stack, dynamic-programming, greedy, 2d-array, stack  

# Description:
#   Given a 2D binary matrix filled with '0's and '1's, find the largest rectangle containing only 1's 
#   and return its area.
#
# Approach:
#   - Treat each row as the base of a histogram.
#   - Build up the histogram heights row by row.
#   - For each row, compute the largest rectangle area in the histogram using a monotonic stack.
#   - Use a helper function to calculate the Largest Rectangle in Histogram (LeetCode 84).
#
# Time Complexity:
#   - O(m * n) where m is the number of rows and n is the number of columns.
#   - Each row is processed in O(n) time for the histogram area.
#
# Space Complexity:
#   - O(n) for histogram heights and stacks used in computation.

from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        def maxHistogramArea(heights: List[int]) -> int:
            N = len(heights)
            NSL = [-1] * N  # Nearest Smaller to Left
            NSR = [N] * N   # Nearest Smaller to Right
            stack = []

            # Compute NSL
            for i in range(N):
                while stack and stack[-1][1] >= heights[i]:
                    stack.pop()
                NSL[i] = stack[-1][0] if stack else -1
                stack.append((i, heights[i]))

            # Reset and compute NSR
            stack = []
            for i in range(N - 1, -1, -1):
                while stack and stack[-1][1] >= heights[i]:
                    stack.pop()
                NSR[i] = stack[-1][0] if stack else N
                stack.append((i, heights[i]))

            # Calculate max area
            maxArea = 0
            for i in range(N):
                width = NSR[i] - NSL[i] - 1
                maxArea = max(maxArea, heights[i] * width)
            return maxArea

        cols = len(matrix[0])
        heights = [0] * cols
        maxRectangle = 0

        for row in matrix:
            for j in range(cols):
                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            area = maxHistogramArea(heights)
            maxRectangle = max(maxRectangle, area)

        return maxRectangle
