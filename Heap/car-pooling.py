# Author: Sparsha Srinath
# Date: 2025-06-29
# Problem: Car Pooling
# Link: https://leetcode.com/problems/car-pooling/
# Tags: Heap, Greedy, Priority Queue, Sorting, Interval
# Time Complexity: O(n log n), where n = number of trips (due to sorting and heap operations)
# Space Complexity: O(n) for the heap

from typing import List
import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Step 1: Sort trips based on start time
        trips.sort(key=lambda t: t[1])

        minHeap = []  # stores [end_location, num_passengers]
        curPass = 0   # current number of passengers in the car

        for trip in trips:
            numPass, start, end = trip

            # Step 2: Remove all trips from heap that have ended before or at this trip's start
            while minHeap and start >= minHeap[0][0]:
                ended_trip = heapq.heappop(minHeap)
                curPass -= ended_trip[1]

            # Step 3: Add current trip's passengers
            curPass += numPass

            # Step 4: If over capacity, return False
            if curPass > capacity:
                return False

            # Step 5: Push current trip into heap
            heapq.heappush(minHeap, [end, numPass])

        # All trips accommodated within capacity
        return True
