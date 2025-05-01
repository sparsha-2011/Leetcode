# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/swim-in-rising-water/
# Date: 2025-04-30
# Tags: graph, dijkstra, heap, priority-queue, grid-traversal, pathfinding

import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        visit = set()
        directions = [[0, -1], [1, 0], [-1, 0], [0, 1]]

        # Min-heap: (time, row, col)
        minH = [(grid[0][0], 0, 0)]
        visit.add((0, 0))

        while minH:
            t, r, c = heapq.heappop(minH)

            # Destination reached
            if r == N - 1 and c == M - 1:
                return t

            # Explore neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in visit:
                    heapq.heappush(minH, [max(grid[nr][nc], t), nr, nc])
                    visit.add((nr, nc))
