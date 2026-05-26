# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/number-of-closed-islands/
# Date: 2026-05-25
# Tags: matrix, dfs, graph, flood-fill
# Description:
#   Given a grid where 0 is land and 1 is water, count the number of closed islands.
#   A closed island is a group of 0s completely surrounded by water (1s) — it does
#   not touch the grid boundary. First, mark all land connected to the border as
#   invalid using DFS (set to -1). Then count remaining islands using standard DFS.
#
# Input: grid (List[List[int]])
# Output: int — number of closed islands
#
# Example:
#   Input : grid=[[1,1,1,1,1,1,1,0],
#                  [1,0,0,0,0,1,1,0],
#                  [1,0,1,0,1,1,1,0],
#                  [1,0,0,0,0,1,0,1],
#                  [1,1,1,1,1,1,1,0]]
#   Output: 2
#
# Time Complexity : O(m * n) — visit each cell at most once
# Space Complexity: O(m * n) — visited sets and recursion stack

from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit_mark = set()
        visit = set()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        islands = 0

        def dfs_mark(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit_mark or grid[r][c] == 1:
                return
            visit_mark.add((r, c))
            grid[r][c] = -1
            for dr, dc in directions:
                dfs_mark(r + dr, c + dc)

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit or grid[r][c] == 1:
                return
            visit.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # First column and last column
        for r in range(ROWS):
            if grid[r][0] == 0 and (r, 0) not in visit_mark:
                dfs_mark(r, 0)
            if grid[r][COLS - 1] == 0 and (r, COLS - 1) not in visit_mark:
                dfs_mark(r, COLS - 1)

        # First and last row
        for c in range(COLS):
            if grid[0][c] == 0 and (0, c) not in visit_mark:
                dfs_mark(0, c)
            if grid[ROWS - 1][c] == 0 and (ROWS - 1, c) not in visit_mark:
                dfs_mark(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0 and (r, c) not in visit:
                    dfs(r, c)
                    islands += 1

        return islands
