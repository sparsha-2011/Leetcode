# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/reconstruct-itinerary/
# Date: 2025-04-23
# Tags: graph, dfs, backtracking, priority-queue, min-heap

import heapq
from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Step 1: Build graph using a min-heap to ensure lexicographical order
        graph = defaultdict(list)
        for src, dest in tickets:
            heapq.heappush(graph[src], dest)

        route = []

        # Step 2: DFS traversal from "JFK"
        def dfs(node):
            while graph[node]:
                # Pop the next lexicographically smallest destination
                next_node = heapq.heappop(graph[node])
                dfs(next_node)
            route.append(node)

        # Step 3: Start DFS from "JFK"
        dfs("JFK")

        # Step 4: Reverse the route to get the correct itinerary order
        return route[::-1]
