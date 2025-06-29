# Author: Sparsha Srinath
# Leetcode: https://leetcode.com/problems/longest-valid-parentheses/
# Tags: Stack, Greedy, String
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        Computes the length of the longest valid (well-formed) parentheses substring.

        Args:
            s (str): The input string consisting of '(' and ')'.

        Returns:
            int: Length of the longest valid parentheses substring.
        """
        stack = [-1]  # Initialize with base index
        max_len = 0   # Store the maximum valid substring length

        for i, c in enumerate(s):
            if c == '(':
                # Push index of '(' onto the stack
                stack.append(i)
            else:
                # Pop the last index
                stack.pop()
                
                if not stack:
                    # No base to match with, push current index as new base
                    stack.append(i)
                else:
                    # Found a valid substring, update max_len
                    max_len = max(max_len, i - stack[-1])

        return max_len
