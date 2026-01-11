# LeetCode Problem: https://leetcode.com/problems/number-of-islands/

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Given a 2D grid map of '1's (land) and '0's (water), count the number of islands.
        An island is surrounded by water and is formed by connecting adjacent lands 
        horizontally or vertically. You may assume all four edges of the grid are 
        all surrounded by water.

        Args:
        grid (List[List[str]]): 2D list representing the map

        Returns:
        int: Number of islands
        """
        if not grid or not grid[0]:
            return 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # Down, Up, Right, Left
        ROWS, COLS = len(grid), len(grid[0])
        num_islands = 0

        def dfs(r: int, c: int):
            # Base case for invalid index or water cell
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"  # Mark as visited

            # Visit all four directions
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Iterate over each cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    num_islands += 1  # Count new island

        return num_islands
