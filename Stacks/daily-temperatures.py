# Author: Sparsha Srinath  
# URL: https://leetcode.com/problems/daily-temperatures/  
# Date: 2025-06-15  
# Tags: monotonic-stack, arrays, temperature, greedy, stack, span-problem  

# Description:
#   Given a list of daily temperatures, return a list where each element represents
#   the number of days you have to wait until a warmer temperature. If there is no future day 
#   for which this is possible, put 0 instead.
#
# Approach:
#   - Use a monotonic decreasing stack that stores pairs: (index, temperature)
#   - Traverse the array in reverse (right to left)
#   - For each day, pop from the stack until you find a warmer day
#   - The span is calculated as the difference in indices
#   - If the stack is empty, no warmer day exists → answer is 0
#
# Example:
#   Input : temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
#   Output:               [1, 1, 4, 2, 1, 1, 0, 0]
#
# Time Complexity: O(n) — each element is pushed and popped at most once
# Space Complexity: O(n) — for the stack and result list

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # Stack stores (index, temperature)

        for i in range(len(temperatures) - 1, -1, -1):
            # Pop all colder or same-temp days from stack
            while stack and stack[-1][1] <= temperatures[i]:
                stack.pop()
            
            if stack:
                res[i] = stack[-1][0] - i  # Days until next warmer
            else:
                res[i] = 0  # No warmer day ahead
            
            stack.append((i, temperatures[i]))  # Push current day
        
        return res
