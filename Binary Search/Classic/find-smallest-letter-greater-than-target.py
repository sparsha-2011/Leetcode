
# Author: Sparsha Srinath
# Date: 2025-08-10
# Problem: Find Smallest Letter Greater Than Target
# Link: https://leetcode.com/problems/find-smallest-letter-greater-than-target/
# Tags: Binary Search, Array
# Time Complexity: O(log n) - Binary search on sorted letters
# Space Complexity: O(1) - Constant extra space


from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        N = len(letters)
        start = 0
        end = N - 1

        while start <= end:
            mid = (start + end) // 2
            if target >= letters[mid]:
                start = mid + 1
            else:
                end = mid - 1

        return letters[start % N]


