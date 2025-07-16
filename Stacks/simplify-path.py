# Author: Sparsha Srinath
# Date: 2025-06-29
# Problem: Simplify Path
# Leetcode URL: https://leetcode.com/problems/simplify-path/
# Tags: Stack, String
# Time Complexity: O(n), where n is the length of the input path
# Space Complexity: O(n), for the stack used to build the simplified path

class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []           # Stack to store valid directory names
        file_name = ''       # Temporary variable to build directory names or special tokens

        # Add a trailing '/' to handle the last segment uniformly
        for c in path + '/':
            if c == '/':
                if file_name == '..':
                    # ".." means move one directory up, so pop from stack if possible
                    if stack:
                        stack.pop()
                    file_name = ''
                elif file_name == '.':
                    # "." refers to the current directory, so just ignore
                    file_name = ''
                elif file_name:
                    # Any valid directory name, push it to the stack
                    stack.append(file_name)
                    file_name = ''
            else:
                # Build the current directory name character by character
                file_name += c
                
        # Join all valid directories with '/' to form the simplified path
        return "/" + "/".join(stack)
