# Date: 2025-04-15
# Author: Sparsha Srinath
# Leetcode: https://leetcode.com/problems/rotting-oranges/
# Tags: BFS, Graph, Matrix, Queue, Simulation

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Get the number of rows and columns
        ROWS, COLS = len(grid), len(grid[0])

        # Directions: right, down, up, left
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        # Initialize variables
        minutes = 0  # Time taken to rot all oranges
        fresh = 0    # Count of fresh oranges
        q = deque()  # Queue for BFS

        # First pass: count fresh oranges and collect rotten ones
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        # BFS to rot adjacent fresh oranges minute by minute
        while fresh > 0 and q:
            qLen = len(q)
            for _ in range(qLen):
                row, col = q.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    # Check bounds and whether the orange is fresh
                    if (0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1):
                        # Rot the orange
                        grid[r][c] = 2
                        q.append((r, c))
                        fresh -= 1
            # One minute has passed after processing the current layer
            minutes += 1

        # If all fresh oranges have rotted, return the time taken; else return -1
        return minutes if fresh == 0 else -1
