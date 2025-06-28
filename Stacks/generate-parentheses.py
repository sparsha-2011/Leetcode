# Author: Sparsha Srinath
# Leetcode Problem: https://leetcode.com/problems/generate-parentheses/
# Tags: Backtracking, Recursion, String
# Time Complexity: O(4^n / √n)
# Space Complexity: O(n) for recursion stack

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generate all combinations of well-formed parentheses for `n` pairs.

        Args:
            n (int): Number of pairs of parentheses.

        Returns:
            List[str]: All valid combinations of n pairs of parentheses.
        """
        res = []
        stack = []

        def backtrack(openN: int, closedN: int) -> None:
            # Base case: when we’ve used up all pairs
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            # If we can still add an open parenthesis
            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closedN)
                stack.pop()
            
            # If we can add a closing parenthesis (only if it won't invalidate the string)
            if closedN < openN:
                stack.append(')')
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res
