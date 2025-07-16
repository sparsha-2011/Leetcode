# Author: Sparsha Srinath
# Date: 2025-06-29
# Problem: Simplify Path
# Source: Leetcode - https://leetcode.com/problems/simplify-path/
# Tags: Stack, String
# Time Complexity: O(n), where n is the length of the input path
# Space Complexity: O(n), for the stack used to build the simplified path

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []      # Stack to hold valid directory names
        cur = ""        # Current directory name being built

        # Iterate through each character in the path plus an extra '/' to finalize last token
        for c in path + "/":
            if c == "/":
                if cur == "..":
                    # ".." means go up one directory if possible
                    if stack:
                        stack.pop()
                elif cur != "" and cur != ".":
                    # Ignore empty tokens and current directory symbol
                    stack.append(cur)
                cur = ""  # Reset current token after a segment ends
            else:
                cur += c  # Build up the current token

        # Join all valid segments to form the canonical path
        return "/" + "/".join(stack)
