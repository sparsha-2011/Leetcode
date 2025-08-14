# Author: Sparsha Srinath
# Date: 2025-08-13
# Problem: Koko Eating Bananas
# Link: https://leetcode.com/problems/koko-eating-bananas/
# Tags: Binary Search, Math
# Time Complexity: O(n log m)  # n = number of piles, m = max pile size
# Space Complexity: O(1)

from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        start = 1
        res = -1
        end = max(piles)

        def isValid(mid):
            if not mid:
                return False
            time = 0
            for i in piles:
                time += (i + mid - 1) // mid
            return time <= h

        while start <= end:
            mid = (start + end) // 2
            if isValid( mid):
                res = mid
                end = mid - 1
            else:
                start = mid + 1
        
        return res
