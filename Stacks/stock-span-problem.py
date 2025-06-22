# Author: Sparsha Srinath  
# Problem: Stock Span Problem  
# Date: 2025-06-15  
# Tags: arrays, monotonic-stack, span-problem, stack, greedy  
# URL: https://practice.geeksforgeeks.org/problems/stock-span-problem-1587115621/  

# Description:
#   The stock span problem is a financial problem where we have a series of daily stock prices,
#   and we need to calculate the span of the stock’s price for all days.
#   The span of the stock’s price on a given day is defined as the maximum number of consecutive
#   days just before the given day, for which the price of the stock on the current day is greater 
#   than or equal to its price on the previous days.
#
# Approach:
#   - Use a monotonic decreasing stack to keep track of indices of prices
#   - For each day, pop from the stack until we find a previous day with a higher price
#   - The span is calculated as the difference in indices
#   - If no greater element is found to the left, span is i + 1
#
# Time Complexity: O(n) — each price is pushed and popped at most once
# Space Complexity: O(n) — for the stack and the span list

from typing import List

class Solution:
    def calculateSpan(self, prices: List[int]) -> List[int]:
        stack = []  # stores (index, price)
        span = [0] * len(prices)

        for i, price in enumerate(prices):
            # Pop while the top price is less than or equal to current
            while stack and stack[-1][1] <= price:
                stack.pop()
            
            # If no previous greater, span = i + 1
            if not stack:
                span[i] = i + 1
            else:
                span[i] = i - stack[-1][0]
            
            stack.append((i, price))  # Push current day info
        
        return span
