# Author: Sparsha Srinath
# Date: 2025-11-09
# Problem: Path With Minimum Effort
# Link: https://leetcode.com/problems/path-with-minimum-effort/
# Tags: Graph, Dijkstra, Min-Heap, BFS
# Time Complexity: O(R * C * log(R * C))
# Space Complexity: O(R * C)

import heapq
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Min-heap storing (current_effort, row, col)
        minHeap = [(0, 0, 0)]
        visit = set()

        while minHeap:
            e, r, c = heapq.heappop(minHeap)

            if (r, c) in visit:
                continue

            # Reached destination
            if r == ROWS - 1 and c == COLS - 1:
                return e

            visit.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    nr >= 0 and nc >= 0 and
                    nr < ROWS and nc < COLS and
                    (nr, nc) not in visit
                ):
                    newDiff = max(
                        e,
                        abs(heights[r][c] - heights[nr][nc])
                    )
                    heapq.heappush(minHeap, (newDiff, nr, nc))
                
        return -1
