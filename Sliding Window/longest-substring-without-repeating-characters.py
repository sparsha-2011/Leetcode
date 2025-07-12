# Author: Sparsha Srinath
# Date: 2025-06-29
# Leetcode: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Tags: Sliding Window, HashSet, Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(k), where k is the size of the character set
# Description:
#   Find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Returns the length of the longest substring without repeating characters.

        Args:
            s (str): Input string.

        Returns:
            int: Length of the longest substring with all unique characters.
        """
        start = 0
        unique = set()
        maxLen = 0

        for end in range(len(s)):
            if s[end] not in unique:
                unique.add(s[end])
                maxLen = max(maxLen, end - start + 1)
            else:
                # Remove characters from the start until duplicate is removed
                while s[start] != s[end]:
                    unique.remove(s[start])
                    start += 1
                start += 1  # skip the duplicate

        return maxLen
