# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/network-delay-time/
# Date: 2025-04-23
# Tags: dijkstra, graphs, shortest-path, priority-queue, bfs

import heapq
from collections import defaultdict
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Step 1: Build adjacency list
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # Step 2: Initialize distances and min-heap
        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[k] = 0
        visited = set()
        minHeap = [(0, k)]  # (cost, node)

        # Step 3: Dijkstra’s Algorithm
        while minHeap:
            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)

            for neighbor, weight in graph[node]:
                if neighbor not in visited and cost + weight < dist[neighbor]:
                    dist[neighbor] = cost + weight
                    heapq.heappush(minHeap, (dist[neighbor], neighbor))

        # Step 4: Check if all nodes were reached
        return -1 if len(visited) != n else max(dist.values())
