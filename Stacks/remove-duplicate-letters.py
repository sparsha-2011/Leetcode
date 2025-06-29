# Author: Sparsha Srinath
# Leetcode: https://leetcode.com/problems/remove-duplicate-letters/
# Tags: Greedy, Stack, Lexicographical Order
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import defaultdict

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        Removes duplicate letters from the string such that every letter appears 
        once and only once, and the result is the smallest in lexicographical order 
        among all possible results.

        Args:
            s (str): The input string containing lowercase letters.

        Returns:
            str: The lexicographically smallest result string with unique characters.
        """

        stack = []                 # Monotonic stack to build the result
        chars = set()              # Set to keep track of what's already in the result
        freq  = defaultdict(int)   # Frequency map of each character in the string

        # Count the frequency of each character
        for i in s:
            freq[i] += 1

        # Greedy + Stack logic
        for i in s:
            freq[i] -= 1           # We are processing this character, so reduce its count

            if i in chars:
                continue           # Skip if already in result

            # Remove characters that are larger than current and will appear later
            while stack and i < stack[-1] and freq[stack[-1]] > 0:
                chars.remove(stack.pop())

            stack.append(i)
            chars.add(i)

        return "".join(stack)

