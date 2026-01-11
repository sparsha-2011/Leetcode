# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/min-cost-to-connect-all-points/
# Date: 2025-04-23
# Tags: graphs, prims-algorithm, minimum-spanning-tree, greedy, heap

import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        
        # Step 1: Build adjacency list with Manhattan distances
        adj = {i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Step 2: Prim's Algorithm Initialization
        res = 0
        minH = [[0, 0]]  # (cost, node)
        visit = set()

        # Step 3: Construct MST
        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            visit.add(i)
            res += cost
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])

        return res
