# Date: 2025-04-15
# Author: Sparsha Srinath
# Leetcode (Walls and Gates): https://leetcode.com/problems/walls-and-gates/
# Tags: BFS, Graph, Matrix, Shortest Path, Queue

from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Modify the input grid in-place to fill each empty room with the distance 
        to its nearest gate. If a gate is unreachable, the room remains INF.
        """

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        INF = 2147483647  # Representation of an empty room
        q = deque()

        # Step 1: Add all gates (cells with 0) to the BFS queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        # Step 2: Perform BFS from all gates simultaneously
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                row, col = r + dr, c + dc

                # If the neighboring cell is a valid empty room
                if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == INF:
                    # Update the distance from the gate
                    grid[row][col] = grid[r][c] + 1
                    # Add the updated cell to the queue for further expansion
                    q.append((row, col))
