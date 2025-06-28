# Author: Sparsha Srinath
# Leetcode Problem: https://leetcode.com/problems/valid-parentheses/
# Tags: Stack, String
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determines if the input string `s` containing only '(', ')', '{', '}', '[' and ']' 
        is valid. A string is valid if:
        - Open brackets are closed by the same type of brackets.
        - Open brackets are closed in the correct order.

        Args:
            s (str): Input string containing brackets.

        Returns:
            bool: True if the string is valid, False otherwise.
        """

        closeToOpen = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in s:
            if char in closeToOpen:
                # If stack is not empty and top of stack matches expected opening bracket
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                # Push opening bracket onto the stack
                stack.append(char)

        # Valid if no unmatched opening brackets remain
        return not stack
