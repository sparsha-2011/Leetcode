# LeetCode Problem: https://leetcode.com/problems/max-area-of-island/

from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Given a 2D grid of 0s and 1s, return the size of the largest island.
        An island is a group of 1s connected 4-directionally. You may assume 
        all four edges of the grid are surrounded by water (0s).

        Args:
        grid (List[List[int]]): 2D list of 0s and 1s representing the map

        Returns:
        int: Maximum area of an island
        """
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0

        def dfs(r: int, c: int) -> int:
            # Return 0 if out of bounds, water cell, or already visited
            if (
                r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                grid[r][c] == 0 or (r, c) in visited
            ):
                return 0

            visited.add((r, c))  # Mark as visited

            # Explore all 4 directions and count area
            return (
                1 + 
                dfs(r + 1, c) +
                dfs(r - 1, c) +
                dfs(r, c + 1) +
                dfs(r, c - 1)
            )

        # Iterate through the entire grid
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, dfs(r, c))

        return max_area
