# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/count-sub-islands/
# Date: 2026-05-25
# Tags: matrix, dfs, graph
# Description:
#   Given two grids, count islands in grid2 that are sub-islands of grid1.
#   A sub-island is an island in grid2 where every land cell also exists in grid1.
#   Build a sub_grid marking cells as "c" (common — land in both grids) or "s"
#   (only in grid2). First, use DFS to mark all cells connected to any "s" cell
#   as "s" (these islands touch non-common land, so they aren't sub-islands).
#   Then count remaining islands made entirely of "c" cells.
#
# Input: grid1 (List[List[int]]), grid2 (List[List[int]])
# Output: int — number of sub-islands
#
# Example:
#   Input : grid1=[[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
#           grid2=[[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
#   Output: 3
#
# Time Complexity : O(m * n) — visit each cell at most once
# Space Complexity: O(m * n) — sub_grid and visited sets

from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid1), len(grid1[0])
        visit = set()
        visit_mark = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        islands = 0
        sub_grid = [[0] * (COLS) for i in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] == 1 and grid1[r][c] == 1:
                    sub_grid[r][c] = "c"
                elif grid2[r][c] == 1:
                    sub_grid[r][c] = "s"

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visit or sub_grid[r][c] != "c":
                return
            visit.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        def dfs_mark(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visit_mark or sub_grid[r][c] == 0:
                return
            sub_grid[r][c] = "s"
            visit_mark.add((r, c))
            for dr, dc in directions:
                dfs_mark(r + dr, c + dc)

        # Mark all islands connected to non-common cells
        for r in range(ROWS):
            for c in range(COLS):
                if sub_grid[r][c] == "s" and (r, c) not in visit_mark:
                    dfs_mark(r, c)

        # Count remaining islands of only common cells
        for r in range(ROWS):
            for c in range(COLS):
                if sub_grid[r][c] == "c" and (r, c) not in visit:
                    dfs(r, c)
                    islands += 1

        return islands
