
# Author: Sparsha Srinath
# Leetcode Problem: https://leetcode.com/problems/decode-string/
# Tags: Stack, String, Recursion (alternative approach)
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def decodeString(self, s: str) -> str:
        """
        Decodes an encoded string where patterns follow the form k[encoded_string].
        Nested patterns are supported.

        Args:
            s (str): The encoded input string.

        Returns:
            str: The fully decoded string.
        """
        stack = []
        num = 0
        cur_str = ''

        for c in s:
            if c.isdigit():
                # Build the full repeat number (could be more than one digit)
                num = num * 10 + int(c)
            elif c == '[':
                # Push the current context and reset for the nested level
                stack.append((cur_str, num))
                cur_str = ''
                num = 0
            elif c == ']':
                # Pop from stack and build the repeated string
                prev_str, repeat = stack.pop()
                cur_str = prev_str + cur_str * repeat
            else:
                # Accumulate the current string
                cur_str += c

        return cur_str
