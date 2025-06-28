
# Author: Sparsha Srinath
# Leetcode Problem: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
# Tags: Stack, String
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        Removes all adjacent duplicates in a string.

        For every pair of adjacent matching characters, both are removed.
        This process continues until no more duplicates are found.

        Args:
            s (str): Input string containing lowercase letters.

        Returns:
            str: String after removing all adjacent duplicates.
        """
        stack = []

        for c in s:
            # If the top of the stack matches the current character, pop it
            if stack and stack[-1] == c:
                stack.pop()
            else:
                # Otherwise, push the current character
