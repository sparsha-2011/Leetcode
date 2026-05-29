# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/making-a-large-island/
# Date: 2026-05-28
# Tags: matrix, dfs, hash-map, connected-components
# Description:
#   Given a grid of 0s and 1s, flip at most one 0 to 1 to maximize island size.
#   Phase 1: DFS to label each island with a unique ID and record its size.
#   Phase 2: For each 0 cell, check 4 neighbors, collect unique island IDs
#   using a set (to avoid double counting), sum their sizes + 1 (the flipped cell).
#   Track the maximum. Handle all-1s grid by initializing max with existing largest.
#   Island IDs start from 2 to avoid conflict with original grid value 1.
#
# Input: grid (List[List[int]])
# Output: int — largest possible island after flipping one 0
#
# Example:
#   Input : grid=[[1,0],[0,1]]
#   Output: 3
#
# Time Complexity : O(n²) — two passes over the grid
# Space Complexity: O(n²) — visited set and island size map

from collections import defaultdict
from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(r, c, isl_id):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit or grid[r][c] == 0:
                return 0
            visit.add((r, c))
            size = 1
            grid[r][c] = isl_id
            for dr, dc in directions:
                size += dfs(r + dr, c + dc, isl_id)
            return size

        num = 2
        island_size = defaultdict(int)
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visit and grid[r][c] == 1:
                    size = dfs(r, c, num)
                    island_size[num] = size
                    num += 1

        max_island = max(island_size.values()) if island_size else 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    new_size = 1
                    seen = set()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] != 0:
                            isla_num = grid[nr][nc]
                            if isla_num not in seen:
                                seen.add(isla_num)
                                new_size += island_size[isla_num]
                    max_island = max(max_island, new_size)

        return max_island
