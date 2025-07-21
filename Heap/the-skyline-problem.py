# Author: Sparsha Srinath  
# Date: 2025-07-19  
# Problem: The Skyline Problem  
# Link: https://leetcode.com/problems/the-skyline-problem/  
# Tags: Heap, Sweep Line, Priority Queue  
# Time Complexity: O(n log n), where n is the number of events  
# Space Complexity: O(n)  

import heapq
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Step 1: Create critical points (events)
        # Start events: (x=start, height=-H, end=R)
        # End events: (x=end, height=0, end=0)
        events = []
        for L, R, H in buildings:
            events.append((L, -H, R))  # entering building
            events.append((R, 0, 0))   # leaving building
        events.sort()  # sort by x; for same x, entering (-H) comes before leaving (0)

        # Step 2: Use max-heap to track active buildings
        result = []
        heap = [(0, float("inf"))]  # (neg_height, end_x)

        for x, negH, R in events:
            # Remove all buildings from the heap that ended before or at current x
            while heap and heap[0][1] <= x:
                heapq.heappop(heap)

            # If it's a start event, add the building to the heap
            if negH != 0:
                heapq.heappush(heap, (negH, R))

            # Current max height = -heap[0][0]
            curr_max = -heap[0][0]
            # If the height changes from previous key point, record it
            if not result or result[-1][1] != curr_max:
                result.append([x, curr_max])

        return result
