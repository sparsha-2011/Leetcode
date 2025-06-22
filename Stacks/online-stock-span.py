# Author: Sparsha Srinath  
# URL: https://leetcode.com/problems/online-stock-span/  
# Date: 2025-06-15  
# Tags: monotonic-stack, design, arrays, stack, greedy  

# Description:
#   Design a class that collects daily stock prices and returns the span of the stock’s price for the current day.
#   The span of the stock's price today is defined as the maximum number of consecutive days (including today)
#   the price of the stock was less than or equal to today's price.
#
# Approach:
#   - Use a monotonic decreasing stack that stores pairs of (price, span).
#   - When a new price comes in, pop all smaller or equal prices from the stack.
#   - The span for the current price is 1 + the spans of all prices popped.
#   - Push the current price and its calculated span to the stack.
#
# Time Complexity: O(1) amortized per call to next() — each element is pushed and popped at most once.
# Space Complexity: O(n) for storing prices in the stack, where n is number of calls to next().

class StockSpanner:

    def __init__(self):
        # Stack will store tuples of (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        # Pop all prices less than or equal to current and accumulate their spans
        while self.stack and self.stack[-1][0] <= price:
            prev_price, prev_span = self.stack.pop()
            span += prev_span
        
        # Push current price and its span
        self.stack.append((price, span))
        return span
