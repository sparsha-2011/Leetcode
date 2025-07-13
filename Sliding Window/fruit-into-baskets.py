# Author: Sparsha Srinath
# Date: 2025-06-29
# Leetcode: https://leetcode.com/problems/fruit-into-baskets/
# Tags: Sliding Window, HashMap
# Time Complexity: O(n)
# Space Complexity: O(1) — since the number of fruit types is limited
# Description:
#   You are given an array of integers `fruits` where each integer represents a tree with a type of fruit.
#   You can only carry at most two types of fruits at once. Return the length of the longest contiguous
#   subarray containing at most two different types of fruits.

from collections import defaultdict
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        unique = defaultdict(int)
        maxLen = 0

        for end in range(len(fruits)):
            unique[fruits[end]] += 1

            if len(unique) == 2:
                maxLen = max(maxLen, end - start + 1)
            elif len(unique) > 2:
                while len(unique) != 2:
                    unique[fruits[start]] -= 1
                    if unique[fruits[start]] == 0:
                        del unique[fruits[start]]
                    start += 1

        return maxLen if maxLen else len(fruits)
