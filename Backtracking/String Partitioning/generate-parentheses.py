# Date: 2025-04-15
# Author: Sparsha Srinath
# Leetcode Problem: 22. Generate Parentheses
# Link: https://leetcode.com/problems/generate-parentheses/
# Tags: Backtracking, Recursion, DFS

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(cur_str, open_p, close):
            # Base case: if the current string has n opening and n closing parentheses
            if open_p == close == n:
                res.append(cur_str)
                return

            # Add an opening parenthesis if we still have some left to add
            if open_p < n:
                dfs(cur_str + '(', open_p + 1, close)

            # Add a closing parenthesis if it's valid to do so
            if close < open_p:
                dfs(cur_str + ')', open_p, close + 1)

        dfs('', 0, 0)
        return res
