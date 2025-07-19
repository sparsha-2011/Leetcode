# Author: Sparsha Srinath
# Date: 2025-06-29
# Problem: Reorganize String
# Link: https://leetcode.com/problems/reorganize-string/
# Tags: Heap, Greedy, Priority Queue, String, HashMap
# Time Complexity: O(n log k), where n is the length of the input string and k is the number of unique characters
# Space Complexity: O(k) for the heap and frequency dictionary

from collections import defaultdict
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Step 1: Count frequency of each character
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1

        # Step 2: Build a max heap using negative counts
        # (Python heapq is a min-heap by default, so we negate the counts)
        maxHeap = [(-cnt, c) for c, cnt in freq.items()]
        heapq.heapify(maxHeap)

        prev = None  # To keep track of the previously used character
        res = ""     # Final result string

        while maxHeap or prev:
            # If there's a leftover character but nothing to pair with → invalid
            if prev and not maxHeap:
                return ""

            # Step 3: Pop most frequent character
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1  # Decrease count (closer to 0, since cnt is negative)

            # Step 4: Push the previously used character back into heap if it still has occurrences left
            if prev:
                heapq.heappush(maxHeap, prev)

            # Step 5: If current character still has more occurrences, store it as prev for next round
            if cnt != 0:
                prev = (cnt, char)
            else:
                prev = None

        return res
