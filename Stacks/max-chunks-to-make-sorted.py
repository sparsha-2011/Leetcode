# Author: Sparsha Srinath
# Date: 2025-06-29
# Leetcode: https://leetcode.com/problems/max-chunks-to-make-sorted/
# Tags: Stack, Greedy, Array
# Time Complexity: O(n)
# Space Complexity: O(n)
# Description:
#   Given a permutation of [0, 1, ..., n - 1], this function returns
#   the maximum number of chunks such that sorting each chunk
#   individually and concatenating them results in the fully sorted array.

from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        Computes the maximum number of chunks such that sorting each chunk individually
        and concatenating the results yields the fully sorted array.

        Args:
            arr (List[int]): The input array representing a permutation.

        Returns:
            int: The maximum number of valid chunks.
        """
        stack = []

        for num in arr:
            if not stack or stack[-1] <= num:
                # Safe to start a new chunk
                stack.append(num)
            else:
                # Merge chunks: pop until num fits, then push the max seen so far
                max_val = stack.pop()
                while stack and stack[-1] > num:
                    stack.pop()
                stack.append(max_val)

        return len(stack)
