# Author: Sparsha Srinath
# Date: 2025-06-29
# Problem: Reorganize String
# Link: https://leetcode.com/problems/reorganize-string/
# Tags: Heap, Greedy, String, HashMap
# Time Complexity: O(n log k) where n is the length of the string and k is the number of unique characters
# Space Complexity: O(n + k) for the heap, queue, and result

from collections import defaultdict, deque
import heapq
from typing import List

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Step 1: Count frequency of each character
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1

        # Step 2: Create a max heap based on frequency (-ve for max-heap behavior)
        maxHeap = [(-cnt, c) for c, cnt in freq.items()]
        heapq.heapify(maxHeap)

        # Queue to track characters that are in "cooldown" (waiting to be reused)
        q = deque()  # Stores tuples: (count, char, time to reinsert)
        res = []
        i = 0  # Simulates time steps

        while maxHeap or q:
            # Step 3: Reinsert character from cooldown if its wait time is over
            if q and q[0][2] <= i:
                cnt, c, _ = q.popleft()
                heapq.heappush(maxHeap, (cnt, c))

            # Step 4: Use the character with the highest remaining frequency
            if maxHeap:
                cnt, c = heapq.heappop(maxHeap)
                res.append(c)
                cnt += 1  # Decrease count (remember cnt is negative)

                # If there's still some of that character left, add it to cooldown
                if cnt:
                    q.append((cnt, c, i + 2))  # Wait for 1 char gap
            else:
                # If heap is empty but queue still has items, we cannot proceed
                return ""

            i += 1  # Move forward in time

        return ''.join(res)
