# Author: Sparsha Srinath
# Date: 2025-06-29
# GFG: https://www.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1
# Tags: Sliding Window, Queue, Deque
# Time Complexity: O(n)
# Space Complexity: O(k)

from collections import deque

class Solution:
    def firstNegInt(self, arr, k):
        """
        Finds the first negative integer in every window of size k.

        Args:
            arr (List[int]): The input array.
            k (int): Size of the sliding window.

        Returns:
            List[int]: List containing the first negative number in each window. If none, returns 0.
        """
        res = []
        q = deque()  # holds indices of negative numbers
        start = 0

        for end in range(len(arr)):
            if arr[end] < 0:
                q.append(end)
            
            if end - start + 1 == k:
                if q:
                    res.append(arr[q[0]])
                else:
                    res.append(0)
                
                if q and q[0] == start:
                    q.popleft()
                start += 1

        return res
