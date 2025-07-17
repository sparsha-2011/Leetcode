# Author: Sparsha Srinath
# Date: 2025-06-29
# Problem: Basic Calculator II
# Source: Leetcode - https://leetcode.com/problems/basic-calculator-ii/
# Tags: Stack, String, Math, Simulation
# Time Complexity: O(n), where n is the length of the input string
# Space Complexity: O(n), for the stack used to hold intermediate results

class Solution:
    def calculate(self, s: str) -> int:
        op = "+"          # Initial operation
        stack = []        # Stack to store intermediate results
        s += op           # Append an operator to flush the last number
        num = 0           # Current number being processed
        s = s.replace(' ', '')  # Remove all whitespace

        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)  # Accumulate digit into full number
            else:
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "*":
                    stack.append(stack.pop() * num)
                elif op == "/":
                    numerator = stack.pop()
                    # Use int() for truncation towards zero
                    stack.append(int(numerator / num))
                
                op = c      # Update current operator
                num = 0     # Reset number for next digit sequence

        return sum(stack)  # Final result is the sum of the stack
