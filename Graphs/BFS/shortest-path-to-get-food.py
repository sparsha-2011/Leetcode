# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/shortest-path-to-get-food/
# Date: 2026-05-25
# Tags: matrix, bfs, graph, shortest-path
# Description:
#   Given a grid with a start location (*), food cells (#), free spaces (O),
#   and obstacles (X), find the shortest path from start to any food cell.
#   Use BFS level-by-level — each level is one step. When a neighbor is food,
#   return path + 1 (current level + one more step). If the queue empties
#   without finding food, return -1.
#
# Input: grid (List[List[str]])
# Output: int — shortest path to food, or -1 if unreachable
#
# Example:
#   Input : grid=[["X","X","X","X","X","X"],
#                  ["X","*","O","O","O","X"],
#                  ["X","O","O","#","O","X"],
#                  ["X","X","X","X","X","X"]]
#   Output: 3
#
# Time Complexity : O(m * n) — visit each cell at most once
# Space Complexity: O(m * n) — visited set and queue

from typing import List
from collections import deque

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visit = set()
        path = 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "*":
                    q.append((r, c))
                    visit.add((r, c))

        while q:
            qLen = len(q)
            for i in range(qLen):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr <= ROWS - 1 and 0 <= nc <= COLS - 1 and (nr, nc) not in visit:
                        if grid[nr][nc] == '#':
                            return path + 1
                        if grid[nr][nc] == 'O':
                            q.append((nr, nc))
                            visit.add((nr, nc))
