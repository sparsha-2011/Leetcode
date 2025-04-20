# Date: 2025-04-15
# Author: Sparsha Srinath
# Leetcode: https://leetcode.com/problems/pacific-atlantic-water-flow/
# Tags: BFS, Graph, Matrix, Flood Fill, Multi-Source BFS

from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Get the number of rows and columns in the matrix
        ROWS, COLS = len(heights), len(heights[0])
        
        # Directions to move: right, down, up, left
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        # Initialize visited matrices for Pacific and Atlantic oceans
        pac = [[False] * COLS for _ in range(ROWS)]
        atl = [[False] * COLS for _ in range(ROWS)]

        def bfs(starts: List[tuple], ocean: List[List[bool]]):
            """Performs BFS from multiple starting points and marks reachable cells."""
            q = deque(starts)
            while q:
                r, c = q.popleft()
                ocean[r][c] = True  # Mark the cell as reachable from the ocean
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # Check bounds, visit status, and elevation condition
                    if (0 <= nr < ROWS and 0 <= nc < COLS and 
                        not ocean[nr][nc] and 
                        heights[nr][nc] >= heights[r][c]):
                        q.append((nr, nc))

        # Cells adjacent to the Pacific Ocean (top and left edges)
        pacific_starts = [(r, 0) for r in range(ROWS)] + [(0, c) for c in range(COLS)]
        
        # Cells adjacent to the Atlantic Ocean (bottom and right edges)
        atlantic_starts = [(r, COLS - 1) for r in range(ROWS)] + [(ROWS - 1, c) for c in range(COLS)]

        # Run BFS for both oceans
        bfs(pacific_starts, pac)
        bfs(atlantic_starts, atl)

        # Collect cells that can reach both oceans
        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    result.append([r, c])

        return result
