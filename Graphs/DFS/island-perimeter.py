# Author: Sparsha Srinath
# Date: 2025-11-09
# Problem: Island Perimeter
# Link: https://leetcode.com/problems/island-perimeter/
# Tags: DFS, Grid, Graph Traversal
# Time Complexity: O(R * C)
# Space Complexity: O(R * C) due to recursion stack and visited set

from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                return 1
            if (i, j) in visit:
                return 0

            visit.add((i, j))
            perim = dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i - 1, j)
            return perim

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    return dfs(i, j)
        return 0
