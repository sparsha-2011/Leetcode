# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/k-closest-points-to-origin/
# Date: 2025-06-15
# Tags: heap, sorting, geometry, priority-queue, k-closest, euclidean-distance
#
# Description:
#   Given an array of points where points[i] = [xi, yi], and an integer k,
#   return the k closest points to the origin (0, 0).
#
#   The distance between two points is the Euclidean distance:
#       √(x^2 + y^2)
#
#   Approach:
#     - Use a Max Heap of size k to track the k closest points.
#     - Push the negative of the distance so Python's min-heap simulates a max-heap.
#     - Pop from heap when it exceeds k to maintain only the closest points.
#
# Input:
#   points: List[List[int]] — list of coordinates
#   k: int — number of closest points to return
# Output:
#   List[List[int]] — the k closest points to (0, 0)
#
# Example:
#   Input : points = [[1,3],[-2,2]], k = 1
#   Output: [[-2,2]]
#
# Time Complexity: O(n log k)
# Space Complexity: O(k)

import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for x, y in points:
            distance = (x ** 2 + y ** 2) ** 0.5  # Euclidean distance
            heapq.heappush(max_heap, (-distance, [x, y]))

            if len(max_heap) > k:
                heapq.heappop(max_heap)

        # Extract only the coordinates from the heap entries
        return [entry[1] for entry in max_heap]


# -----------------------------
# Optional test case to run
# -----------------------------
if __name__ == "__main__":
    sol = Solution()
    result = sol.kClosest([[1, 3], [-2, 2], [5, 8], [0, 1]], 2)
    print("K Closest Points:", result)  # Output: [[-2, 2], [0, 1]] (order may vary)
