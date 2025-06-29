# Author: Sparsha Srinath
# Leetcode Problem: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
# Tags: Stack, String
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Removes the minimum number of invalid parentheses to make the input string valid.

        A valid parentheses string is defined by matching pairs of '(' and ')' in the correct order.

        Args:
            s (str): The input string containing lowercase letters and parentheses.

        Returns:
            str: A valid string with the minimum number of parentheses removed.
        """
        stack = []
        invalid_indices = set()

        # First pass: identify unmatched ')' and store unmatched '(' indices
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    invalid_indices.add(i)

        # Add remaining unmatched '(' indices to invalid set
        invalid_indices.update(stack)

        # Build the result string excluding characters at invalid indices
        return ''.join(c for i, c in enumerate(s) if i not in invalid_indices)
