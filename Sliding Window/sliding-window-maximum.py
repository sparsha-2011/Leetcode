# Author: Sparsha Srinath
# Date: 2025-06-29
# Leetcode: https://leetcode.com/problems/sliding-window-maximum/
# Tags: Sliding Window, Monotonic Queue, Deque
# Time Complexity: O(n)
# Space Complexity: O(k)

from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Finds the maximum in every sliding window of size k.

        Args:
            nums (List[int]): The input array.
            k (int): The size of the sliding window.

        Returns:
            List[int]: List of maximums for each window.
        """
        result = []
        q = deque()  # Stores indices of potential max values in decreasing order
        start = 0

        for end in range(len(nums)):
            # Remove elements smaller than the current one from the back
            while q and nums[end] > nums[q[-1]]:
                q.pop()

            q.append(end)

            # If window size is reached
            if end - start + 1 == k:
                result.append(nums[q[0]])  # The front of the deque is the max

                # Remove the element going out of the window
                if q[0] == start:
                    q.popleft()
                
                start += 1

        return result
