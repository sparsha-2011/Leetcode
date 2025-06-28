
# Author: Sparsha Srinath
# Leetcode Problem: https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Tags: Stack, Math
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Evaluate the value of an arithmetic expression in Reverse Polish Notation.

        Supported operators are '+', '-', '*', and '/'.
        Division should truncate toward zero.

        Args:
            tokens (List[str]): The list of tokens in RPN.

        Returns:
            int: The result of evaluating the expression.
        """
        stack = []

        for token in tokens:
            if token in {'+', '-', '*', '/'}:
                a = stack.pop()
                b = stack.pop()

                if token == '+':
                    stack.append(b + a)
                elif token == '-':
                    stack.append(b - a)
                elif token == '*':
                    stack.append(b * a)
                elif token == '/':
                    # Python division truncates toward negative infinity with //
                    # So use int() to truncate toward zero
                    stack.append(int(b / a))
            else:
                stack.append(int(token))

        return stack[0]
