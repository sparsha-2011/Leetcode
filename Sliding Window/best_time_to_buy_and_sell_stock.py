# Author: Sparsha Srinath
# Date: 2025-06-29
# Leetcode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Tags: Greedy, Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
# Description:
#   Given an array `prices` where prices[i] is the price of a given stock on the i-th day,
#   return the maximum profit you can achieve from a single buy and sell.
#   You must buy before you sell.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        start = 0

        for end in range(len(prices)):
            if prices[end] - prices[start] >= 0:
                max_prof = max(max_prof, prices[end] - prices[start])
            else:
                while prices[end] - prices[start] < 0:
                    start += 1
                    
        return max_prof
